from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator

from courses_module.models import Courses
from employee_module.views.base.manage_user_view import ManageUserView


class ManageCoursesView(ManageUserView):
    template_name = 'profiles/employee/course/manage_courses_view.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        local_context = {'courses': Courses.objects.all(),
                         'username': request.user.username,
                         'avatar': request.user.avatar,
                         }
        local_context.update(self.context)
        return render(request, self.template_name, local_context)
