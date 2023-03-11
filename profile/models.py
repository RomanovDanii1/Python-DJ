from django.db import models
from cart.models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm\


class EditProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('password1',)
