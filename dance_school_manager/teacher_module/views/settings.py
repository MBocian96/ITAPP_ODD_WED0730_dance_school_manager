from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from authentication_module.models import CustomUser



class SettingsViews(View):
    template_name = 'profiles/teacher/settings.html'

    def get(self, request, customuser_id: int):
        teacher = get_object_or_404(CustomUser, id=customuser_id) #pobieram konkretnego nauczyciela o podanym id jesli go nie ma to strona z 404

