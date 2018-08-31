from django.shortcuts import render
from Client.models import Client
from django.contrib.auth.decorators import login_required
from django.http import Http404

def client_detail(request, nic_name):
    # grab the object...
    client = Client.objects.get(nic_name=nic_name)

    # and pass to the template
    return render(request, 'client_detail.html', {'client': client,})

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
            #client.slug = slugify(thing.name)

            # save the object
            client.save()

            # redirect to our newly created thing
            return redirect('client_detail', slug=thing.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'create_client.html', {
        'form': form,
    })


@login_required
def edit_client(request, slug):
    # grab the object...
    client = Client.objects.get(slug=slug)

    # make sure the logged in user is the owner of the thing
    if Client.user != request.user:
        raise Http404

    # set the form we're using...
    form_class = ThingForm

    # if we're coming to this view from a submitted form,
    # do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=client)

    # and render the template
    return render(request, 'edit_client.html', {
        'client': client,
        'form': form,
    })
