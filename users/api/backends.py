from django.contrib.auth.backends import BaseBackend
from ..models import User

class CustomAuthentication:
    def authenticate(self, email=None, password=None):
        # attempt to get user from the given email
        user = User.objects.get(email=email)
        if user is not None and user.check_password(password):
            if user.is_active:
                return User
            else:
                return "User has not been activated"
        
        # if no user exists or password is wrong
        else:
            return None

        pass

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None