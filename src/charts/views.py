from django.shortcuts import render
from datetime import date, timedelta
from django.utils import timezone
from tickets.models import Ticket

def charts(request):
    bugs_count = Ticket.objects.filter(ticket_type="Bug Report").count()
    features_count = Ticket.objects.filter(ticket_type="Feature Request").count()
    todo_count = Ticket.objects.filter(status="To-Do (Not Started)").count()
    in_progress_count = Ticket.objects.filter(status="In Progress").count()
    completed_count = Ticket.objects.filter(status="Completed").count()

    # Date range for bugs/features updated daily/weekl/monthly
    startdate = date.today() - timedelta(days=30)
    enddate = date.today()
    updated_tickets = Ticket.objects.filter(last_updated__range=[startdate, enddate]).count()
    weekly_updated = updated_tickets / 4
    daily_updated = updated_tickets / 30

    context = {
        "bugs_count": bugs_count,
        "features_count": features_count,
        "todo_count": todo_count,
        "in_progress_count": in_progress_count,
        "completed_count": completed_count,
        "updated_tickets": updated_tickets,
        "weekly_updated": weekly_updated,
        "daily_updated": daily_updated
    }
    return render(request, "charts.html", context)
