from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserUpdateForm,
    ProfileUpdateForm)


def superuser(request):
    """ Allows access to the Admin Panel for superusers """
    if request.user.is_superuser:
        return redirect(reverse("superuser"))


def index(request):
    """ Return the index.html file """
    return render(request, "index.html")


@login_required()
def logout(request):
    """ Logs the user out """
    auth.logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect(reverse("login"))


def login(request):
    """ Return a login page """
    if request.user.is_authenticated:
        return redirect(reverse("index"))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST["username"],
                password=request.POST["password"])

            if user:
                auth.login(user=user, request=request)            
                messages.success(request, "You have logged in successfully.")
                return redirect(reverse("profile"))
            else:
                messages.error(request, "Your username or password is incorrect.")
    else:
        login_form = UserLoginForm()

    return render(request, "login.html", {"login_form": login_form})


def registration(request):
    """ Render the registration page """
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(
                username=request.POST["username"],
                password=request.POST["password1"])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have registered successfully")
                return redirect(reverse("profile"))
            else:
                messages.error(request,
                    "There has been an error with your registration.\
                    Please try again.")

    else:
        registration_form = UserRegistrationForm()

    return render(
        request, "registration.html",
        {"registration_form": registration_form})


@login_required
def profile(request):
    """ The user's profile page """
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile was updated successfully")
            return redirect(reverse("profile"))
    else:
        user_form = UserUpdateForm(
            instance=request.user)
        profile_form = ProfileUpdateForm(
            instance=request.user.profile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "profile": user
    }
    return render(request, "profile.html", context)
