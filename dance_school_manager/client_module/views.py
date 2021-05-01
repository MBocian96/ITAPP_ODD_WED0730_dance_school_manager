from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView

from authentication_module.forms import EditProfileForm

from client_module.models import CustomUser


# Create your views here.
class ClientView(View):
    template_name = 'profiles/student/student_profile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        logged_user = CustomUser.objects.get(user=request.user)  # logged_user = request.user

        context = {'user': logged_user}
        return render(request, self.template_name, context=context)


class ClientSettingsView(View):

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profiles/student/student_profile.html')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profiles/student/student_profile_settings.html', args)
