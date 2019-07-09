from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm


@login_required
def new_bug(request):
    if request.method == "POST":
        new_ticket_form = TicketForm(request.POST)
        if new_ticket_form.is_valid():
            new_ticket_form.instance.raised_by = request.user
            new_ticket_form.instance.ticket_type = "Bug Report"
            new_bug = new_ticket_form.save()
            return redirect(ticket_detail, new_bug.pk)
    else:
        new_ticket_form = TicketForm()

    return render(
        request,
        "new_bug.html",
        {"new_ticket_form": new_ticket_form}
    )

@login_required
def new_feature(request):
    if request.method == "POST":
        new_ticket_form = TicketForm(request.POST)
        if new_ticket_form.is_valid():
            new_ticket_form.instance.raised_by = request.user
            new_ticket_form.instance.ticket_type = "Feature Request"
            new_feature = new_ticket_form.save()
            return redirect(ticket_detail, new_feature.pk)
    else:
        new_ticket_form = TicketForm()

    return render(
        request,
        "new_feature.html",
        {"new_ticket_form": new_ticket_form}
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


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    return render(
        request,
        "ticket_detail.html",
        {"ticket": ticket}
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


def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()

    return redirect(all_tickets)
