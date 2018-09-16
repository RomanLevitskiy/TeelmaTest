from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from OrderApp.models import Order
from Client.models import Client

class ClientOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('subject', 'body', 'price')


class ManagerOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('subject', 'body', 'price')
        #fields = ('subject', 'body', 'price', 'customers')


class ManagerAddClientInOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customers']
"""
class ManagerAddClientInOrderForm(forms.Form):
    client = forms.ModelMultipleChoiceField(queryset=Client.objects.all())
"""
