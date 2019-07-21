from django.conf.urls import url
from .views import (
    new_bug,
    new_feature,
    all_tickets,
    ticket_detail,
    edit_ticket,
    delete_ticket,
    create_comment,
    upvote,
    downvote
)

urlpatterns = [
    url(r'^$', all_tickets, name="all_tickets"),
    url(r'^new/bug$', new_bug, name="new_bug"),
    url(r'^new/feature$', new_feature, name="new_feature"),
    url(r'^details/(?P<pk>\d+)', ticket_detail, name="ticket_detail"),
    url(r'^upvote/(?P<pk>\d+)', upvote, name="upvote"),
    url(r'^downvote/(?P<pk>\d+)', downvote, name="downvote"),
    url(r'^edit/(?P<pk>\d+)', edit_ticket, name="edit_ticket"),
    url(r'^add-comment/(?P<pk>\d+)', create_comment, name="create_comment"),
    url(r'^delete/(?P<pk>\d+)', delete_ticket, name="delete_ticket"),
]
