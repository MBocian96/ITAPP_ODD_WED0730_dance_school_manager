from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator

from authentication_module.models import CustomUser
from employee_module.views.employee_main_view import EmployeeView


class ManageTeachersView(EmployeeView):
    template_name = 'profiles/employee/teacher/manage_teachers_view.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        local_context = {'teachers': CustomUser.objects.filter(is_teacher=True),
                         'username': request.user.username,
                         'avatar': request.user.avatar,
                         }
        local_context.update(self.context)
        return render(request, self.template_name, local_context)
