from django.conf.urls import url
from .views import new_ticket, all_tickets, ticket_detail, edit_ticket, delete_ticket

urlpatterns = [
    url(r'^$', all_tickets, name="all_tickets"),
    url(r'^new/$', new_ticket, name="new_ticket"),
    url(r'^details/(?P<pk>\d+)', ticket_detail, name="ticket_detail"),
    url(r'^edit/(?P<pk>\d+)', edit_ticket, name="edit_ticket"),
    url(r'^delete/(?P<pk>\d+)', delete_ticket, name="delete_ticket"),
]
