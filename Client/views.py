from django.shortcuts import render, redirect
from .models import Client
from Client.forms import ClientForm

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
