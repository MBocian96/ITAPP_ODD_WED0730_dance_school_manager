from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from authentication_module.forms import EditProfileForm
# Create your views here.


# Client can view his courses with descriptions, hyperlink to settings
class ClientView(CreateView):
    template_name = 'profiles/student/student_profile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {'user': request.user,
                   'courses_list': request.user.courses.all()
                   }

        return render(request, self.template_name, context=context)



# Client can edit parameters given in field
class ClientSettingsView(UpdateView):
    form = UserChangeForm
    template_name = 'profiles/student/student_profile_settings.html'
    success_url = reverse_lazy('client_module:user_view')
    fields = {'email', 'username'}

    def get_object(self):
        return self.request.user



#Client can leave course (deletes course from the database not just client's list, fuck)
def AbandonCourse(request, pk):
    user = request.user
    to_delete = user.courses.get(id=pk)
    context = {'item': to_delete}
    if request.method == "POST":
        to_delete.delete()
        return redirect('client_module:user_view')

    return render(request, 'profiles/student/abandon_course.html', context)











