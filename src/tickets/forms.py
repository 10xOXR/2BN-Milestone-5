from django import forms
from django.contrib.auth.models import User
from .models import Ticket


class TicketForm(forms.ModelForm):
    """ Displays the Ticket form """

    title = forms.CharField(
        label="Title",
        max_length=50,
        widget=forms.TextInput(),
        required=True
    )
    description = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(),
        required=True
    )

    class Meta:
        model = Ticket
        fields = [
            "title",
            "description",
        ]
