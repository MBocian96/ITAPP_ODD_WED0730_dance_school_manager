from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


class EmployeeView(View):
    template = 'profiles/employee/employee_main_view.html'
    context = {'manage_courses': '/employee/manage_courses',
               'manage_students': '/employee/manage_students',
               'manage_teachers': '/employee/manage_teachers'
               }

    @method_decorator(login_required)
    def get(self, request):
        local_context = {}
        local_context.update({'username': request.user.username,
                              'avatar': request.user.avatar,
                              })
        local_context.update(self.context)
        return render(request, self.template, context=local_context)
