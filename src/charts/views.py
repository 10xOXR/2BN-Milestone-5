from django.shortcuts import render
from datetime import date, timedelta
from django.utils import timezone
from tickets.models import Ticket
import pytz

def charts(request):
    bug_reports = Ticket.objects.filter(ticket_type=1)
    feature_requests = Ticket.objects.filter(ticket_type=2)
    
    bug_status = [
        item["status"] for item in bug_reports.values("status")
    ]
    bug_todo_count = bug_status.count(1)
    bug_in_progress_count = bug_status.count(2)
    bug_completed_count = bug_status.count(3)

    feature_status = [
        item["status"] for item in feature_requests.values("status")
    ]
    feature_todo_count = feature_status.count(1)
    feature_in_progress_count = feature_status.count(2)
    feature_completed_count = feature_status.count(3)

    # Date range for bugs/features updated daily/weekly/monthly
    updated_bugs = [int(item["last_updated"].timestamp()) for item in bug_reports.values("last_updated")]
    updated_features = [int(item["last_updated"].timestamp()) for item in feature_requests.values("last_updated")]

    now = int(timezone.now().timestamp())
    today = now - int(timedelta(days=1).total_seconds())
    week = now - int(timedelta(days=7).total_seconds())
    month = now - int(timedelta(days=30).total_seconds())

    bug_daily_updated = len(list(x for x in updated_bugs if x in range(today, now)))
    bug_weekly_updated = len(list(x for x in updated_bugs if x in range(week, now)))
    bug_monthly_updated = len(list(x for x in updated_bugs if x in range(month, now)))

    feature_daily_updated = len(list(x for x in updated_features if x in range(today, now)))
    feature_weekly_updated = len(list(x for x in updated_features if x in range(week, now)))
    feature_monthly_updated = len(list(x for x in updated_features if x in range(month, now)))

    context = {
        "bug_todo_count": bug_todo_count,
        "bug_in_progress_count": bug_in_progress_count,
        "bug_completed_count": bug_completed_count,
        "bug_daily_updated": bug_daily_updated,
        "bug_weekly_updated": bug_weekly_updated,
        "bug_monthly_updated": bug_monthly_updated,
        "feature_todo_count": feature_todo_count,
        "feature_in_progress_count": feature_in_progress_count,
        "feature_completed_count": feature_completed_count,
        "feature_daily_updated": feature_daily_updated,
        "feature_weekly_updated": feature_weekly_updated,
        "feature_monthly_updated": feature_monthly_updated
    }
    return render(request, "charts.html", context)
