from registration.backends.simple.views import RegistrationView

# my new registration view, subclassing RegistrationView
# from our plugin
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return ('registration_create_client')
