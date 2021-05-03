from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import  generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from authentication_module.forms import EditProfileForm

from authentication_module.models import CustomUser



class SettingsViews(View):
    template_name = 'profiles/teacher/settings.html'

    def get(self, request, customuser_id: int):
        teacher = get_object_or_404(CustomUser, id=customuser_id) #pobieram konkretnego nauczyciela o podanym id jesli go nie ma to strona z 404

