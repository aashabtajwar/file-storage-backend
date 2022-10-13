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

    # gets the user
    # this method is by default needed for authentication backends
    def get_user(self, user_id):
        try:
            # return User.objects.get(pk=user_id)
            return get_object_or_404(User, pk=user_id)
        except User.DoesNotExist:
            return None


class TokenJWT:
    # method to generate tokens
    # the secret is used from here for now, but will be used a different one in future
    def generateJWT(self, username, email, user_id):
        access_token = self.generateAccessToken(username, email, user_id)
        refresh_token = self.generateRefreshToken(user_id)
        
        return access_token, refresh_token

    # method for generating access token
    def generateAccessToken(self, username, email, user_id):
        # the claims will be username, email and expiration time
        # the algorithm is HS256
        token =jwt.encode(
            {
                "exp": time.time() + 3600,
                "username": username,
                "email": email,
                "id" : user_id,
                "type": "access",
            },
            secret,
            algorithm="HS256"
        )
        return token

    # mothod for generating refresh token
    def generateRefreshToken(self, user_id):
        # refresh token
        # create refresh token in a way 
        # such that it cannot be used as an access token 
        # (i.e. client cannot use it to gain access to routes)
        token = jwt.encode(
            {
                "exp" : time.time() + 86400,
                "id" : user_id,
                "type": "refresh"
            },
            secret,
            algorithm="HS256"
        )
        return token
