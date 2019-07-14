from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


TICKET_STATUS = (
    ("To-Do (Not Started)", "To-Do (Not Started)"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed")
)

class Ticket(models.Model):
    """ Structure of a Bug Ticket """
    title = models.CharField(
        max_length=50,
        blank=False
    )
    ticket_type = models.CharField(
        max_length=20,
        blank=False,
        null=True
    )
    description = models.TextField(
        max_length=1000,
        blank=False
    )
    raised_on = models.DateTimeField(
        auto_now_add=True
    )
    raised_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    last_updated = models.DateTimeField(
        default=timezone.now
    )
    upvotes = models.IntegerField(
        default=0
    )
    status = models.CharField(
        max_length=20,
        choices=TICKET_STATUS,
        default="To-Do (Not Started)"
    )

    def __str__(self):
        return "#{0} [{1}] - {2}".format(self.id, self.ticket_type, self.title)


class Comment(models.Model):
    """ Structure of a single comment """
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        null=True
    )
    comment_text = models.TextField(
        max_length=2000,
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return "Comment {0} on Ticket {1}".format(self.id, self.ticket)


class Upvote(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return "Upvote #{0} on Ticket {1}".format(self.id, self.ticket)
