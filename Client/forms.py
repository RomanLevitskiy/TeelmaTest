from django.forms import ModelForm
from Client.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('nic_name', 'description',)
