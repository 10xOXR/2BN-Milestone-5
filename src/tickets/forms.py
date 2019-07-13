from django import forms
from .models import Ticket, Comment


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


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        required=True
    )

    class Meta:
        model = Comment
        fields = [
            "comment_text"
        ]

class PaymentForm(forms.Form):
    """ Displays the Payment form """

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2030)]

    credit_card_number = forms.CharField(
        label="Credit Card Number",
        required=False
    )
    cvv = forms.CharField(
        label="Card CVV",
        required=False
        )
    expiry_month = forms.ChoiceField(
        label="Month",
        choices=MONTH_CHOICES,
        required=False
    )
    expiry_year = forms.ChoiceField(
        label="Year",
        choices=YEAR_CHOICES,
        required=False
    )
    stripe_id = forms.CharField(
        widget=forms.HiddenInput
    )
