from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404
from .models import Ticket, TicketStatus, TicketType
from .forms import TicketForm, CommentForm
from .views import (
    all_tickets,
    create_comment,
    delete_ticket,
    downvote,
    edit_ticket,
    new_bug,
    new_feature,
    ticket_detail,
    upvote
)

# FORM TESTS


class TestTicketForm(TestCase):

    def test_form_is_valid(self):
        form = TicketForm({
            "title": "Test Ticket",
            "description": "Test description"
        })
        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        form = CommentForm({
            "comment_text": "Test text"
        })
        self.assertTrue(form.is_valid())


# VIEWS TESTS

class TestTicketsViews(TestCase):
    def setUp(self):
        TicketStatus.objects.create(ticket_status="To-Do (Not Started)")
        TicketStatus.objects.create(ticket_status="In Progress")
        TicketType.objects.create(ticket_type="Bug Report")
        TicketType.objects.create(ticket_type="Feature Request")
        previous = Client(
            HTTP_REFERER='http://127.0.0.1:8000/tickets/',
        )
        Ticket.objects.create(
            title="Test Bug",
            description="Test description1",
            # status_id=1,
            status=TicketStatus(id=1),
            ticket_type=TicketType(id=1)).save()
        Ticket.objects.create(
            title="Test Feature",
            description="Test description2",
            status=TicketStatus(id=1),
            ticket_type=TicketType(id=2)).save()
        self.client.post(
            "/users/register/",
            {"email": "Test@Email.com",
                "username": "TestUser",
                "first_name": "TestFirst",
                "last_name": "TestLast",
                "password1": "Testtest1",
                "password2": "Testtest1"})

    def test_all_tickets(self):
        page = self.client.get("/tickets/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tickets.html")

    def test_ticket_detail(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        response = self.client.get(
            "/tickets/details/{0}".format(ticket.pk), follow=True)
        self.assertIn(b"Updated:", response.content)

    def test_tickets_new_bug(self):
        self.client.post(
            "/tickets/new/bug",
            {"title": "Another Bug",
                "description": "Test description3",
                "status_id": "1",
                "ticket_type_id": "1"})
        ticket = Ticket.objects.filter(title="Another Bug")[0]
        self.assertEqual("Another Bug", ticket.title)

    def test_tickets_upvote_bug(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        upvotes = ticket.upvotes
        self.assertEqual(upvotes, 0)
        self.client.get(
            "/tickets/upvote/{0}".format(ticket.pk), follow=True)
        upvote = Ticket.objects.filter(title="Test Bug")[0].upvotes
        self.assertEqual(upvote, 1)

    def test_tickets_upvote_remove(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        upvotes = ticket.upvotes
        self.assertEqual(upvotes, 0)
        self.client.get(
            "/tickets/upvote/{0}".format(ticket.pk), follow=True)
        upvote = Ticket.objects.filter(title="Test Bug")[0].upvotes
        self.client.get(
            "/tickets/downvote/{0}".format(ticket.pk), follow=True)
        downvote = Ticket.objects.filter(title="Test Bug")[0].upvotes
        self.assertEqual(downvote, 0)

    def test_tickets_upvote_feature_with_payment(self):
        ticket = Ticket.objects.filter(title="Test Feature")[0]
        response = self.client.get(
            "/tickets/details/{0}#modal-feature-upvote".format(ticket.pk),
            follow=True)
        self.assertIn(
            b"There is a \xe2\x82\xac5 fee to upvote a Feature",
            response.content)

    def test_tickets_edit(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        response = self.client.get(
            "/tickets/edit/{0}".format(ticket.pk), follow=True)
        self.assertIn(
            b'<h1 class="center-align purple-text text-darken-3 upper"',
            response.content)

    def test_tickets_edit_saved(self):
        ticket = Ticket.objects.filter(
            description="Test description1")[0]
        self.assertEqual(ticket.title, "Test Bug")
        self.client.post("/tickets/edit/{0}".format(ticket.pk), data={
            "title": "Test Bug Updated",
            "description": "Test description on new Bug Ticket"}, follow=True)
        new_ticket_title = Ticket.objects.filter(
            description="Test description on new Bug Ticket")[0].title
        self.assertEqual(new_ticket_title, "Test Bug Updated")

    def test_tickets_delete(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        response = self.client.get(
            "/tickets/{0}".format(ticket.pk), follow=True)
        results = Ticket.objects.filter(
            description="Test description1").count()
        self.assertEqual(results, 1)
        self.client.get("/tickets/delete/{0}".format(ticket.pk), follow=True)
        tickets_delete = Ticket.objects.filter(title="Test Bug").count()
        self.assertEqual(tickets_delete, 0)
