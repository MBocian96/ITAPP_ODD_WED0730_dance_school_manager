from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from django.utils.decorators import method_decorator

# Create your views here.
from django.views.generic import CreateView


class EmployeeView(CreateView):
    template = 'profiles/employee/employee_profile_view.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {'manage_courses': 'manage_courses',
                   'manage_students': 'manage_students',
                   'manage_teachers': 'manage_teachers',
                   'username': request.user.username,
                   'avatar': request.user.avatar,
                   }

        return render(request, self.template, context=context)
