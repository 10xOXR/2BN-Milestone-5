from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Ticket, Comment, Upvote, TicketStatus, TicketType
from users.models import Profile
from .forms import TicketForm, CommentForm
from django.conf import settings
import stripe
from urllib.parse import urlparse

stripe.api_key = settings.STRIPE_SECRET


def all_tickets(request):
    """
    Displays all tickets to the user in the Tickets page, with all
    necessary pagination.
    """

    page = request.GET.get("page", 1)
    ticket_status_list = TicketStatus.objects.all()
    ticket_type_list = TicketType.objects.all()
    tkt_status = request.GET.get("tkt_status")
    tkt_type = request.GET.get("tkt_type")
    tickets = Ticket.objects.all()
    tickets = (
        tickets.filter(status__id=tkt_status) if tkt_status else tickets
    )
    tickets = (
        tickets.filter(ticket_type__id=tkt_type) if tkt_type else tickets
    )

    paginator = Paginator(tickets, 4)
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

    context = {
        "tickets": tickets,
        "ticket_status_list": ticket_status_list,
        "ticket_type_list": ticket_type_list,
        "tkt_status": tkt_status,
        "tkt_type": tkt_type,
    }
    return render(
        request,
        "tickets.html",
        context
    )


@login_required
def new_bug(request):
    """
    Renders the New Bug page and redirects to the Ticket Detail
    page when successfully submitted.
    """

    if request.method == "POST":
        bug_form = TicketForm(request.POST)
        if bug_form.is_valid():
            bug_form.instance.raised_by = request.user
            bug_form.instance.ticket_type_id = "1"
            bug_form.instance.status_id = "1"
            new_bug = bug_form.save()
            return redirect(ticket_detail, new_bug.pk)
    else:
        bug_form = TicketForm()

    context = {
        "bug_form": bug_form
    }
    return render(
        request,
        "new_bug.html",
        context
    )


@login_required
def new_feature(request):
    """
    Renders the New Feature page, takes payment from user, and redirects
    to the Ticket Detail page when successfully submitted.
    """

    if request.method == "POST":
        feature_form = TicketForm(request.POST)

        if feature_form.is_valid():
            try:
                token = request.POST["stripeToken"]
                customer = stripe.Charge.create(
                    amount=1000,
                    currency="EUR",
                    description=(
                        "Feature Request: " +
                        request.user.get_full_name() +
                        " (" + request.user.email + ")"),
                    source=token,
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                    messages.success(request, "You have successfully paid!")
                    feature_form.instance.raised_by = request.user
                    feature_form.instance.ticket_type_id = "2"
                    feature_form.instance.status_id = "1"
                    new_feature = feature_form.save()
                    return redirect(ticket_detail, new_feature.pk)
            else:
                messages.error(request, "Unable to take payment!")
        else:
            messages.error(
                request, "Unable to take a payment with that card!"
            )
    else:
        feature_form = TicketForm()

    context = {
        "feature_form": feature_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    }
    return render(
        request,
        "new_feature.html",
        context
    )


@login_required
def create_comment(request, pk):
    """
    Processes comments added via the Ticket Detail page and redirects back
    to the same page after successfully posting comment.
    """
    if request.method == "POST":
        parent_ticket = get_object_or_404(Ticket, pk=pk)
        new_comment = CommentForm(request.POST)
        if new_comment.is_valid():
            new_comment.instance.author = request.user
            new_comment.instance.ticket = parent_ticket
            new_comment.save()
        return redirect(
            ticket_detail,
            parent_ticket.pk
        )


def ticket_detail(request, pk):
    """
    Collects information related to a single ticket and renders the
    Ticket Detail page.
    """

    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    comments = Comment.objects.filter(ticket_id=ticket.pk)
    upvotes = Upvote.objects.filter(ticket_id=ticket.pk).values("user_id")
    voters = [vote["user_id"] for vote in upvotes]
    ticket_status_list = TicketStatus.objects.all()
    tkt_status = ticket.status.id
    new_comment = CommentForm()

    context = {
        "ticket": ticket,
        "comments": comments,
        "voters": voters,
        "publishable": settings.STRIPE_PUBLISHABLE,
        "ticket_status_list": ticket_status_list,
        "tkt_status": tkt_status,
        "new_comment": new_comment
    }
    return render(
        request,
        "ticket_detail.html",
        context
    )


@login_required
def admin_status_update(request, pk):
    """
    Allows Admin users to change the current status of a ticket on
    the Ticket Detail page.
    """

    ticket = get_object_or_404(Ticket, pk=pk)
    tkt_status = request.GET.get("tkt_status")
    ticket.views -= 1
    ticket.save()
    Ticket.objects.filter(id=ticket.pk).update(
        status=int(tkt_status), last_updated=timezone.now()
    )
    messages.success(request, "Ticket status updated!")
    return redirect(
        ticket_detail,
        ticket.pk
    )


@login_required
def upvote(request, pk):
    """
    Processes upvotes on the Ticket Detail page and handles payments
    where the upvote occurs on a Feature Request.
    """

    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    ticket.views -= 1
    ticket.save()
    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            customer = stripe.Charge.create(
                amount=500,
                currency="EUR",
                description=(
                    "Feature Upvote: " +
                    request.user.get_full_name() +
                    " (" + request.user.email + ")"),
                source=token,
            )
        except stripe.error.CardError:
            messages.error(request, "Your card was declined!")
        if customer.paid:
                messages.success(request, "You have successfully paid!")
                Upvote.objects.create(
                    ticket_id=ticket.pk,
                    user_id=request.user.id
                )
                return redirect(ticket_detail, ticket.pk)
        else:
            messages.error(request, "Unable to take payment!")
    else:
        Upvote.objects.create(
            ticket_id=ticket.pk,
            user_id=request.user.id
        )
    return redirect(
        ticket_detail,
        ticket.pk
    )


@login_required
def downvote(request, pk):
    """
    Processes downvotes on the Ticket Detail page.
    """

    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes -= 1
    ticket.views -= 1
    ticket.save()
    Upvote.objects.filter(
        ticket_id=ticket.pk,
        user_id=request.user.id
    ).delete()
    return redirect(
        ticket_detail,
        ticket.pk
    )


@login_required
def edit_ticket(request, pk):
    """
    Renders the Edit Ticket page and populates the form fields with
    the pre-existing data from the ticket stored in the database.
    """

    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        edit_ticket = TicketForm(request.POST, instance=ticket)
        if edit_ticket.is_valid():
            edit_ticket.instance.last_updated = timezone.now()
            edit_ticket.save()
            messages.success(request, "Ticket updated successfully!")
            return redirect(ticket_detail, ticket.pk)
    else:
        edit_ticket = TicketForm(instance=ticket)

    context = {
        "edit_ticket": edit_ticket
    }
    return render(
        request,
        "edit_ticket.html",
        context
    )


@login_required
def delete_ticket(request, pk):
    """
    Deletes a specified ticket.
    """

    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()

    return redirect(all_tickets)
