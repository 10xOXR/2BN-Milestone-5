from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import NewTicketForm


@login_required
def new_ticket(request):
    if request.method == "POST":
        new_ticket_form = NewTicketForm(request.POST)
        if new_ticket_form.is_valid():
            new_ticket_form.instance.raised_by = request.user
            new_ticket_form.save()
            return redirect(all_tickets)
    else:
        new_ticket_form = NewTicketForm()

    return render(
        request,
        "newticket.html",
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
