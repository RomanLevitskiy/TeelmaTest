from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from ManagerApp.forms import ManagerForm
from django.contrib.auth.models import User
from ManagerApp.models import Manager

@login_required(login_url='/accounts/register/')
def manager_base(request):
    return render(request, 'manager_base.html')

@login_required(login_url='/accounts/register/')
def create_manager(request):
    form_class = ManagerForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                request.POST['username'],
                request.POST['email'],
                request.POST['password1'],
                is_active = True
                )
            # create an instance but don't save yet
            manager = Manager()
            manager.nic_name = request.POST['nic_name']
            manager.description = request.POST['description']
            manager.user = new_user
            manager.save()
            return redirect('create_manager_comlete')
    else:
        form = form_class()

    return render(request, 'create_manager.html', {
        'form': form,
    })

def create_manager_comlete(request):
    return render(request, 'create_manager_comlete.html')
