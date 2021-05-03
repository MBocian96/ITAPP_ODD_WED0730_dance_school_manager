from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from authentication_module.models import CustomUser


class ManageUserView(View):
    template = 'profiles/employee/employee_home_view.html'
    context = {'home_view': '/employee/',
               'manage_courses': '/employee/manage_courses',
               'manage_students': '/employee/manage_students',
               'manage_teachers': '/employee/manage_teachers'
               }
    filter_arg = {}

    @method_decorator(login_required)
    def get(self, request):
        local_context = self.get_default_context(request)

        return render(request, self.template, context=local_context)

    def get_default_context(self, request):
        local_context = {'users': CustomUser.objects.filter(**self.filter_arg),
                         'username': request.user.username,
                         'avatar': request.user.avatar,
                         }
        local_context.update(self.context)
        return local_context
