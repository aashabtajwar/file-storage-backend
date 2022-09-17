from typing import Type
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.conf import settings

from datetime import datetime, timedelta

# Create your models here.


class UserManager(BaseUserManager):

    # create a normal user
    def create_user(self, first_name, last_name, username, email, password = None):
        if username is None:
            raise TypeError('Users should have a username')
        
        if email is None:
            raise TypeError('No email was given')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save()
        return user 

    # create super user
    def create_superuser(self, first_name, last_name, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(username, first_name, last_name, email)
        user.is_superuser = True 
        user.is_staff = True 
        user.save()
        return user 

## AbstractBaseUser is selected because we want to write
## all the fields for a user model from scratch

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_verified = models.BooleanField(default=False) # will not be verified at first
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
