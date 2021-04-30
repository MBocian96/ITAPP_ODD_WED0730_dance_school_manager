from django.shortcuts import render
from django.views import generic


# Create your views here.
class UserView(generic.ListView):
    pass
# template_name = client_module/user.html

class UserSettingsView(generic.ListView):
    pass