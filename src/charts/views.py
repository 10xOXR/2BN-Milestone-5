from django.shortcuts import render
from datetime import date, timedelta
from django.utils import timezone
from tickets.models import Ticket
import pytz

def charts(request):
    bugs_count = Ticket.objects.filter(ticket_type_id=1).count()
    features_count = Ticket.objects.filter(ticket_type_id=2).count()
    todo_count = Ticket.objects.filter(status_id=1).count()
    in_progress_count = Ticket.objects.filter(status_id=2).count()
    completed_count = Ticket.objects.filter(status_id=3).count()

    # Date range for bugs/features updated daily/weekl/monthly
    startdate = timezone.now() - timedelta(days=30)
    enddate = timezone.now()
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
