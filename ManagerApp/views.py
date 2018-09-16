from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from ManagerApp.forms import ManagerForm
from django.contrib.auth.models import User
from OrderApp.forms import ManagerOrderForm, ManagerAddClientInOrderForm
from ManagerApp.models import Manager
from OrderApp.models import Order

@login_required(login_url='/accounts/register/')
def manager_base(request):
    all_orders = Order.objects.all().order_by('date_create')
    return render(request, 'manager_base.html', {'all_orders': all_orders})

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



@login_required(login_url='/accounts/register/')
def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        form = ManagerOrderForm(request.POST, instance=order)
        if form.is_valid():
            edit_order = form.save(commit=False)
            edit_order.subject = request.POST['subject']
            edit_order.body = request.POST['body']
            edit_order.price = request.POST['price']
            edit_order.save()
            return redirect('manager_base')
    else:
        form = ManagerOrderForm(instance=order)
    return render(request, 'manager_edit_order.html', {'form': form})


@login_required(login_url='/accounts/register')
def add_client_in_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        form = ManagerAddClientInOrderForm(request.POST, instance=order)
        if form.is_valid():
            edit_order = form.save(commit=False)
            edit_order.customers.add(request.POST['customers'])
            edit_order.save()
            return redirect('manager_base')
    else:
        form = ManagerAddClientInOrderForm(instance=order)
    return render(request, 'manager_add_client_in_order.html', {'form': form})
