from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    nic_name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.OneToOneField(User, blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.nic_name

    class Meta:
        ordering = ('nic_name',)
