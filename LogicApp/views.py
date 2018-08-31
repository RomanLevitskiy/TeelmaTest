from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from Client.models import Client

def index(request):
    clients = Client.objects.all()

    return render(request, 'index.html', {'clients':clients})
