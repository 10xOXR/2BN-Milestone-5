from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TicketStatus(models.Model):
    """ Structure of a Ticket Status """

    TICKET_STATUS_OPTIONS = (
        ("To-Do (Not Started)", "To-Do (Not Started)"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed")
    )
    ticket_status = models.CharField(
        max_length=20,
        choices=TICKET_STATUS_OPTIONS
    )

    class Meta:
        verbose_name = ("Ticket Status")
        verbose_name_plural = ("Ticket Status")

    def __str__(self):
        return self.ticket_status


class TicketType(models.Model):
    """ Structure of a Ticket Types """

    TICKET_STATUS_OPTIONS = (
        ("Bug Report", "Bug Report"),
        ("Feature Request", "Feature Request")
    )
    ticket_type = models.CharField(
        max_length=15,
        choices=TICKET_STATUS_OPTIONS
    )

    class Meta:
        verbose_name = ("Ticket Type")
        verbose_name_plural = ("Ticket Types")

    def __str__(self):
        return self.ticket_type


class Ticket(models.Model):
    """ Structure of a Ticket """

    title = models.CharField(
        max_length=50,
        blank=False
    )
    ticket_type = models.ForeignKey(
        TicketType,
        null=False
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
    views = models.IntegerField(
        default=0
    )
    status = models.ForeignKey(
        TicketStatus,
        default="1"
    )

    class Meta:
        ordering = ("-last_updated", )

    def __str__(self):
        return "#{0} [{1}] - {2}".format(
            self.id, self.ticket_type, self.title
        )


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
    """ Structure of Upvotes """

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
