from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import UserEntity

class UserForm(forms.Form):

        name = forms.CharField(max_length=255)
        email = forms.CharField(max_length=255)
        username = forms.CharField(max_length=255)
        password = forms.CharField(max_length=255)

