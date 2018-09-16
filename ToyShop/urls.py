"""ToyShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from LogicApp import views as LogicAppViews
from LogicApp import urls as LogicAppUrls
from Client.backends import MyRegistrationView
from Client import views as ClientViews
from Client import forms as ClientForms
from ManagerApp import urls as ManagerAppUrls
from Client import urls as ClientAppUrls

urlpatterns = [
    url(r'^manager/', include(ManagerAppUrls)),
    url(r'^client/', include(ClientAppUrls)),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/create_client/$', ClientViews.create_client, name='registration_create_client'),
    #url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_create_client'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', LogicAppViews.index, name='home'),
    url(r'^about/', include(LogicAppUrls)),
    url(r'^admin/', admin.site.urls),
    url(r'^sorted_input_user/', LogicAppViews.sorted_input_user, name='sorted_input_user'),
]
