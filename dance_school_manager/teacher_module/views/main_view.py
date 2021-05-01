from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from django.utils.decorators import method_decorator

# Create your views here.
from django.views.generic import CreateView

class TeacherView(CreateView):
    template = 'profiles/teacher/teacher_profile_view.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {'manage_courses': 'course_names', # CHECK/ADD COURSES LIST OF THIS TEACHER HERE 
                   'username': request.user.username,
                   'avatar': request.user.avatar,
                   }

        return render(request, self.template, context=context)
