from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^create_order/$', views.client_create_order, name="client_create_order"),
    url(r'^create_order_comlete/$', views.client_complited_create_order, name="client_complited_create_order"),
    url(r'^edit_order/(?P<id>\d+)/$', views.edit_order, name="cleint_edit_order"),
    url(r'^delete_order/(?P<id>\d+)/$', views.delete_order, name="cleint_delete_order"),
    url(r'^home/$', views.client_base, name="client_base"),
]
