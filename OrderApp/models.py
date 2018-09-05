from django.contrib.auth.models import User
from Client.models import Client
from django.db import models

class Order(models.Model):
    subject = models.CharField(max_length=250, blank = False)
    body = models.TextField(blank = False)
    price = models.FloatField(blank = False)
    customers = models.ManyToManyField(Client)
    date_create = models.DateField(auto_now_add = True)
    last_changes = models.DateField(auto_now = True)


    def __str__(self):
        return self.subject + "  " + self.last_changes.strftime("%Y-%m-%d %H:%M:%S")
