from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

import datetime
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'user'
        db_table = "user_profile"

    # username = models.CharField(max_length=200, null=False, unique=True, default="vivek777patel")
    date_of_birth = models.DateField(_("Date_of_Birth"), default=datetime.date.today)
    gender = models.IntegerField(null=False, default=1)
    # password = models.CharField(max_length=200, blank=True, default="")

    mobile = models.CharField(max_length=200, blank=True, default="")
    first_name = models.CharField(max_length=200, blank=True, default="")
    middle_name = models.CharField(max_length=200, blank=True, default="")
    last_name = models.CharField(max_length=200, blank=True, default="")

    email = models.EmailField(_('email address'), blank=False, max_length=254, unique=True, default='vivek777patel@gmail.com')

    # is_active = models.IntegerField(default=1, null=False)
    last_login_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    last_visited_location = models.IntegerField(blank=True, null=True)
    favourite_place = models.IntegerField(blank=True, null=True)
    current_profile_pic = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    user_type = models.IntegerField(default=1, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        """A string representation of the model."""
        return self.email

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


'''
    vivek777patel
'''


class UserStatus(models.Model):

    class Meta:
        app_label = 'user'
        db_table = "user_status"

    user_status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200, null=False)
    updated_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_id = models.ForeignKey(User, related_name='user', null=False, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1, null=False)

    def __str__(self):
        """A string representation of the model."""
        return '{0} ({1})'.format(self.user_status_id, self.user_id.email)

