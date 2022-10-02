from django.contrib.auth.backends import BaseBackend
from django.shortcuts import get_object_or_404
from ..models import User

import jwt
import time

secret = "secret"

class CustomAuthentication:
    def authenticate(self, email=None, password=None):
        # attempt to get user from the given email
        user = User.objects.get(email=email)
        if user is not None and user.check_password(password):
            if user.is_active:
                return user
            else:
                return "User has not been activated"
        
        # if no user exists or password is wrong
        else:
            return None

        pass

    def get_user(self, user_id):
        try:
            # return User.objects.get(pk=user_id)
            return get_object_or_404(User, pk=user_id)
        except User.DoesNotExist:
            return None


class TokenJWT:
    def generateJWT(self, username, email):
        encode = jwt.encode({
            "exp": time.time() + 300,
            "username": username,
            "email": email,
        },
        secret,
        algorithm="HS256"
        )
        return encode