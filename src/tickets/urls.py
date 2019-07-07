from django.conf.urls import url
from .views import new_ticket, all_tickets

urlpatterns = [
    url(r'^$', all_tickets, name="all_tickets"),
    url(r'^new/$', new_ticket, name="new_ticket"),
]
