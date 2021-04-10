from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from authentication_module.models import CustomUser, EMPLOYEE, TEACHER, STUDENT, UNKNOWN


class ProfileView(View):
    def get_context_by(self, user_type):
        context_by_user_type = {
            EMPLOYEE: {'manage_courses': 'manage_courses',
                       'manage_students': 'manage_students',
                       'manage_teachers': 'manage_teachers',
                       },
            STUDENT: {},
            TEACHER: {},
        }
        return context_by_user_type[user_type]

    def get_template_path_by(self, user_type) -> str:
        user_type_views = {
            EMPLOYEE: 'employee_profile_view.html',
            TEACHER: 'teacher_profile_view.html',
            STUDENT: 'student_profile_view.html',
            UNKNOWN: None,
        }
        return 'profiles/' + user_type_views[user_type]

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        current_user_type: CustomUser = request.user.get_user_type()

        context = self.get_context_by(current_user_type)
        template = self.get_template_path_by(current_user_type)
        context['username'] = request.user.username
        context['avatar'] = request.user.avatar

        return render(request, template, context=context)
