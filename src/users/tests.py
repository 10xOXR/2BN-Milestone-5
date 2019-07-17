from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserUpdateForm,
    ProfileUpdateForm
)


class TestUserLoginForm(TestCase):
    def test_login_form_valid(self):
        form = UserLoginForm(
            {"username": "TestUser", "password": "Testpassword1"}
        )
        self.assertTrue(form.is_valid())

    def test_correct_error_message_returned(self):
        form = UserLoginForm(
            {"username": "TestUser", "password": ""}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password"], [u"This field is required."])


class TestUserRegistrationForm(TestCase):
    def test_registration_form_is_valid(self):
        form = UserRegistrationForm({
            "username": "TestUser",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@test.com",
            "password1": "Testuser1", 
            "password2": "Testuser1"
        })
        self.assertTrue(form.is_valid())
    
    def test_passwords_do_not_match(self):
        form = UserRegistrationForm({
            "username": "TestUser",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@test.com",
            "password1": "Testuser1", 
            "password2": "Testuser2"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password2"], [u"Passwords must match"])


class TestUserUpdateForm(TestCase):
    def test_first_name_updated(self):
        form = UserUpdateForm({"first_name": "NewName"})
        form.save()
        self.assertTrue(form.is_valid())


class TestProfileUpdateForm(TestCase):
    def test_profile_image_updated(self):
        photo = ProfileUpdateForm
        photo.image = SimpleUploadedFile(
            "test.png", b"file_content", content_type="image/png")
        self.client.post(reverse("profile"), {"photo": photo})
        self.assertIsNotNone(ProfileUpdateForm)

# VIEWS TESTS

class TestIndexView(TestCase):
    def test_index(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")


class TestSuperuserView(TestCase):
    def test_superuser(self):
        page = self.client.get("/admin/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("superuser"))


class TestLoginView(TestCase):
    def test_login(self):
        page = self.client.get("/users/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


class TestLogoutView(TestCase):
    def test_logout(self):
        page = self.client.get("/users/logout/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("login"))


class TestRegisterView(TestCase):
    def test_register_view(self):
        page = self.client.get("/users/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")


class TestProfileView(TestCase):
    def test_profile(self):
        page = self.client.get("/users/profile/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse("profile"))
