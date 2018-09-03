from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^(?P<nic_name>[-\w]+)/$', views.client_detail, name='client_detail'),
    url(r'^home/$', views.manager_base, name="manager_base"),
    url(r'^create/$', views.create_manager, name="manager_create"),
    url(r'^create_manager_comlete/$', views.create_manager_comlete, name="create_manager_comlete"),
]
