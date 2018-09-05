from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Client
from Client.forms import ClientForm
from OrderApp.forms import ClientOrderForm
from django.contrib.auth.decorators import login_required
from OrderApp.models import Order

@login_required(login_url='/accounts/register/')
def client_base(request):
    return render(request, 'client_base.html')

def create_client(request):
    form_class = ClientForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            client = form.save(commit=False)

            # set the additional details
            client.user = request.user
            # save the object
            client.save()

            # redirect to our newly created thing
            #return redirect('client_detail', nic_name=client.nic_name)
            return redirect("home")

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'create_client.html', {
        'form': form,
    })

@login_required(login_url='/accounts/register/')
def client_create_order(request):
    form_client_order = ClientOrderForm
    if request.method == 'POST':
        form = form_client_order(request.POST)
        if form.is_valid():
            try:
                #client = Client.objects.get(Client.user.pk == request.POST.pk)
                new_order = Order()
                new_order.subject = request.POST['subject']
                new_order.body = request.POST['body']
                new_order.price = request.POST['price']
                new_order.save()
                user = User.objects.get(id__exact=request.user.id)
                client = Client.objects.get(user=user)
                new_order.save()
                new_order.customers.add(client)
                order_dict={'subject':new_order.subject, 'body':new_order.body, 'price':new_order.price}
                return redirect('client_complited_create_order', context=order_dict)
            except Client.DoesNotExist:
                return HttpResponse("Your username and password didn't match.")
            """
            new_order = Order(
                request.POST['subject'],
                request.POST['body'],
                request.POST['price'],
                customers = request.User.client;
            )
            new_order.save()
            """
            #return render(request, 'client_complited_create_order.html', order_dict)

    else:
        form = form_client_order()

    return render(request, 'client_create_order.html', {
        'form': form,
    })

def client_complited_create_order(request):
    return render(request, 'client_complited_create_order.html')
