from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from Client.models import Client
from ManagerApp import urls as ManagerAppUrls
from Client import urls as ClientAppUrls
from ManagerApp.models import Manager
from django.contrib.auth.decorators import login_required

def index(request):
    current_user = request.user
    try:
        num_reg_client = Client.objects.filter(user__exact=current_user).count()
        num_reg_manager = Manager.objects.filter(user__exact=current_user).count()
        if client_reg == 1:
            return redirect('client_base')
        elif num_reg_manager == 1:
            return redirect('manager_base')
    except:
        raise Http404("Order does not exist")
    #return render(request, 'index.html')

@login_required(login_url='/accounts/register/')
def sorted_input_user(request):
    current_user = request.user
    #try:
    num_reg_client = Client.objects.filter(user__exact=current_user).count()
    num_reg_manager = Manager.objects.filter(user__exact=current_user).count()
    if num_reg_client == 1:
        return redirect('client_base')#('logic_about_clients')
    elif num_reg_manager == 1:
        return redirect('manager_base')#('logic_about_managers')
    #except:
        #raise Http404("Order does not exist")
