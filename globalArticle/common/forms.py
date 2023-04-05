from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="email")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")