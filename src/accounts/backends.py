from django.contrib.auth.models import User


class EmailAuth():
    """
    Authenticate a user based on an exact match on the email and password
    """

    def authenticate(self, username=None, password=None):
        """
        Get an instance of 'User' based off of the email and verify the
        password
        """

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.pk.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Used by the Django auth system to retreive a user instance """

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.pk.DoesNotExist:
            return None
