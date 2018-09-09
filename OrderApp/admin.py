from django.contrib import admin
from OrderApp.models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('subject', 'date_create', 'last_changes')
    filter_horizontal = ('customers',)

# and register it
admin.site.register(Order, OrderAdmin)
