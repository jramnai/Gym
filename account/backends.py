from django.contrib.auth.models import User
from emailusernames.utils import get_user
import base64
import hashlib


class LoginUsingEmailAsUsernameBackend(object):
    """
    Custom Authentication backend that supports using an e-mail address
    to login instead of a username.
    See: http://blog.cingusoft.org/custom-django-authentication-backend
    """
    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    # def authenticate(self, username=None, password=None):
    #     try:
    #         # Check if the user exists in Django's database
    #         user = User.objects.get(email=username)
    #     except User.DoesNotExist:
    #         return None

    #     # Check password of the user we found
    #     if check_password(password, user.password):
    #         return user
    #     return None

    def _email_to_username(email):
        # Emails should be case-insensitive unique
        email = email.lower()
        # Deal with internationalized email addresses
        converted = email.encode('utf8', 'ignore')
        return base64.urlsafe_b64encode(hashlib.sha256(converted).digest())[:30]

    def get_user(email, queryset=None):
        """
        Return the user with given email address.
        Note that email address matches are case-insensitive.
        """
        if queryset is None:
            queryset = User.objects
        return queryset.get(username=_email_to_username(email))

    def authenticate(self, email=None, password=None, **kwargs):
        if email is None:
            email = kwargs.get('username')

        try:
            user = get_user(email)
            if user.check_password(password):
                user.backend = "%s.%s" % (
                    self.__module__, self.__class__.__name__)
                return user
        except User.DoesNotExist:
            return None

    # Required for the backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
