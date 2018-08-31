from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^(?P<nic_name>[-\w]+)/$', views.client_detail, name='client_detail'),
]
