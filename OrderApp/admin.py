from django.contrib import admin

from OrderApp.models import Order
# set up automated slug creation
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('subject', 'date_create', 'last_changes')

# and register it
admin.site.register(Order, OrderAdmin)
