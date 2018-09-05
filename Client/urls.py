from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^(?P<nic_name>[-\w]+)/$', views.client_detail, name='client_detail'),
    url(r'^home/$', views.client_base, name="client_base"),
    url(r'^create_order/$', views.client_create_order, name="client_create_order"),
    url(r'^create_order_comlete/$', views.client_complited_create_order, name="client_complited_create_order"),
]
