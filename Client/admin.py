from django.contrib import admin

from Client.models import Client

# set up automated slug creation
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('nic_name', 'description',)

# and register it
admin.site.register(Client, ClientAdmin)
