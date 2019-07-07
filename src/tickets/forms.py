from django import forms
from django.contrib.auth.models import User
from .models import Ticket, TICKET_TYPE


class NewTicketForm(forms.ModelForm):
    """ Displays the New Ticket form """

    ticket_type = forms.ChoiceField(
        label="Ticket Type",
        choices=TICKET_TYPE,
        required=True
    )
    title = forms.CharField(
        label="Title",
        max_length=50,
        widget=forms.TextInput(),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea
    )

    class Meta:
        model = Ticket
        fields = [
            "ticket_type",
            "title",
            "description",
        ]
