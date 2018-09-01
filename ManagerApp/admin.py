from django.contrib import admin

from ManagerApp.models import Manager

# set up automated slug creation
class ManagerAdmin(admin.ModelAdmin):
    model = Manager
    list_display = ('nic_name', 'description',)

# and register it
admin.site.register(Manager, ManagerAdmin)
