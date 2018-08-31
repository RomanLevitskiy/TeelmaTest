from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^clients/$', TemplateView.as_view(template_name="about_clients.html"), name="logic_about_clients"),
    url(r'^managers/$', TemplateView.as_view(template_name="about_managers.html"), name="logic_about_managers"),
]
