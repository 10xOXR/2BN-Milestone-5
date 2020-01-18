from django.urls import path, include
from .views import logout, login, registration, profile
from users import urls_reset

urlpatterns = [
    path("logout/", logout, name="logout"),
    path("login/", login, name="login"),
    path("register/", registration, name="register"),
    path("profile/", profile, name="profile"),
    path("password-reset/", include(urls_reset)),
]
