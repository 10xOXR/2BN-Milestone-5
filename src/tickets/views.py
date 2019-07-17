from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ticket, Comment, Upvote
from .forms import TicketForm, CommentForm
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required
def new_bug(request):
    if request.method == "POST":
        bug_form = TicketForm(request.POST)
        if bug_form.is_valid():
            bug_form.instance.raised_by = request.user
            bug_form.instance.ticket_type = "Bug Report"
            new_bug = bug_form.save()
            return redirect(ticket_detail, new_bug.pk)
    else:
        bug_form = TicketForm()

    return render(
        request,
        "new_bug.html",
        {"bug_form": bug_form}
    )


@login_required
def new_feature(request):
    if request.method == "POST":
        feature_form = TicketForm(request.POST)

        if feature_form.is_valid():
            try:
                token = request.POST["stripeToken"]
                customer = stripe.Charge.create(
                    amount = int(100 * 100),
                    currency = "EUR",
                    description = (
                        "Feature Request: "+\
                            request.user.get_full_name() +\
                            " (" + request.user.email + ")"),
                    source=token,
                )
                if customer.paid:
                    messages.success(request, "You have successfully paid!")
                    feature_form.instance.raised_by = request.user
                    feature_form.instance.ticket_type = "Feature Request"
                    new_feature = feature_form.save()
                    return redirect(ticket_detail, new_feature.pk)
                else:
                    messages.error(request, "Unable to take payment!")
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
        else:
            messages.error(request, "Unable to take a payment with that card!")
    else:
        feature_form = TicketForm()

    return render(
        request,
        "new_feature.html",
        {"feature_form": feature_form,
        "publishable": settings.STRIPE_PUBLISHABLE}
    )


def all_tickets(request):
    tickets = Ticket.objects.filter(
        raised_on__lte=timezone.now()
        ).order_by('-raised_on')
    
    return render(
        request,
        "tickets.html",
        {"tickets": tickets}
    )


@login_required
def create_comment(request, pk):
    parent_ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        new_comment = CommentForm(request.POST)
        if new_comment.is_valid():
            new_comment.instance.author = request.user
            new_comment.instance.ticket = parent_ticket
            new_comment.save()
            return redirect(ticket_detail, parent_ticket.pk)
    else:
        new_comment = CommentForm()

    return render(
        request,
        "create_comment.html",
        {"new_comment": new_comment}
    )


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    comments = Comment.objects.filter(ticket_id=ticket.pk)
    upvotes = Upvote.objects.filter(ticket_id=ticket.pk).values("user_id")
    voters = [vote["user_id"] for vote in upvotes]

    return render(
        request,
        "ticket_detail.html",
        {
            "ticket": ticket,
            "comments": comments,
            "voters": voters,
            "publishable": settings.STRIPE_PUBLISHABLE
        }
    )


@login_required
def upvote(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    ticket.views -= 1
    ticket.save()
    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            customer = stripe.Charge.create(
                amount = int(5 * 100),
                currency = "EUR",
                description = (
                    "Feature Upvote: "+\
                        request.user.get_full_name() +\
                        " (" + request.user.email + ")"),
                source=token,
            )
            if customer.paid:
                messages.success(request, "You have successfully paid!")
                Upvote.objects.create(
                    ticket_id=ticket.pk,
                    user_id=request.user.id
                )
                return redirect(ticket_detail, ticket.pk)
            else:
                messages.error(request, "Unable to take payment!")
        except stripe.error.CardError:
            messages.error(request, "Your card was declined!")
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
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        edit_ticket = TicketForm(request.POST, instance=ticket)
        if edit_ticket.is_valid():
            edit_ticket.instance.last_updated = timezone.now()
            edit_ticket.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        edit_ticket = TicketForm(instance=ticket)

    return render(
        request,
        "edit_ticket.html",
        {"edit_ticket": edit_ticket}
    )


@login_required
def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()

    return redirect(all_tickets)
