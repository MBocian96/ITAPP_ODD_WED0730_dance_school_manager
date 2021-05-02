from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.views.generic import CreateView
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
from authentication_module.forms import EditProfileForm


class ClientView(CreateView):
    template_name = 'profiles/student/student_profile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {'user': request.user,
                   'courses_list': request.user.courses.all()
                   }

        return render(request, self.template_name, context=context)

class ClientSettingsView(generic.UpdateView):
    form = UserChangeForm
    template_name = 'profiles/student/student_profile_settings.html'
    success_url = reverse_lazy('user_view')
    fields = {'email', 'username'}

    def get_object(self):
        return self.request.user