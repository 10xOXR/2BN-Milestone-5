from django.urls import path
from .views import (
    new_bug,
    new_feature,
    all_tickets,
    ticket_detail,
    edit_ticket,
    delete_ticket,
    create_comment,
    upvote,
    downvote,
    admin_status_update
)

urlpatterns = [
    path("", all_tickets, name="all_tickets"),
    path("new/bug", new_bug, name="new_bug"),
    path("new/feature", new_feature, name="new_feature"),
    path("details/<int:pk>", ticket_detail, name="ticket_detail"),
    path("upvote/<int:pk>", upvote, name="upvote"),
    path("downvote/<int:pk>", downvote, name="downvote"),
    path("edit/<int:pk>", edit_ticket, name="edit_ticket"),
    path("add-comment/<int:pk>", create_comment, name="create_comment"),
    path("delete/<int:pk>", delete_ticket, name="delete_ticket"),
    path("status-update/<int:pk>",
        admin_status_update, name="admin_status_update"
        ),
]
