"""
from django.forms import ModelForm
from ManagerApp.models import Manager


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ('nic_name', 'description',)
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ManagerForm(UserCreationForm):
    nic_name = forms.CharField(max_length=200, help_text='name for site')
    description = forms.CharField(max_length=200, help_text='litle about manager')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
