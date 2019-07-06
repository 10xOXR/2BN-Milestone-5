from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from accounts.models import Profile


class UserLoginForm(forms.Form):
    """ Form to be used to log users into the site """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """ Form used to register a new user """
    username = forms.CharField(
        min_length=5,
        max_length=15,
        widget=forms.TextInput(),
        required=True)
    first_name = forms.CharField(
        label="First Name",
        min_length=2,
        max_length=30,
        widget=forms.TextInput(),
        required=True)
    last_name = forms.CharField(
        label="Last Name",
        min_length=2,
        max_length=30,
        widget=forms.TextInput(),
        required=True)
    email = forms.CharField(
        label="Email",
        min_length=5,
        max_length=70,
        widget=forms.EmailInput(),
        required=True)
    password1 = forms.CharField(
        label="Password",
        min_length=8,
        max_length=25,
        widget=forms.PasswordInput(),
        required=True,
        validators=[RegexValidator(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9@$!%*?&-]{8,25}$",
            message=(
                "Your password must contain a minimum of a number,\
                    a lowercase and uppercase letter."
            )
        )])
    password2 = forms.CharField(
        label="Password Confirmation",
        min_length=8,
        max_length=25,
        widget=forms.PasswordInput(),
        required=True)

    class Meta:
        model = User
        fields = [
            "username", "first_name",
            "last_name", "email",
            "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("Email address must be unique")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        if password1 != password2:
            raise ValidationError("Passwords must match")
        return password2

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First Name",
        min_length=2,
        max_length=30,
        widget=forms.TextInput(),
        required=False)
    last_name = forms.CharField(
        label="Last Name",
        min_length=2,
        max_length=30,
        widget=forms.TextInput(),
        required=False)
    email = forms.CharField(
        label="Email",
        min_length=5,
        max_length=70,
        widget=forms.EmailInput(),
        required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
