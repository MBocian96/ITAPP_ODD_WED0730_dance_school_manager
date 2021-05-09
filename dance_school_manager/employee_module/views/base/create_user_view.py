from typing import Callable

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.views.base.manage_user_view import ManageUserView


class CreateUserView(ManageUserView):
    template = '/'
    user_form: Callable
    user_role = 'is_'

    @method_decorator(login_required)
    def get(self, request):
        user_form = self.user_form()
        local_context = {'user_form': user_form}
        local_context.update(self.context)
        return render(request, self.template, local_context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        user_form = self.user_form(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            student = CustomUser(username=name, email=email, is_teacher=True)
            courses_not_found = []
            for field in user_form.fields.keys():
                if field.endswith('course'):
                    course_name = user_form.cleaned_data[field]
                    try:
                        self.assign_course_to_user(user=student, course_name=course_name)
                    except Courses.DoesNotExist:
                        courses_not_found.append(course_name)
            if courses_not_found:
                local_context = {'user_form': user_form, 'courses_not_found': courses_not_found}
                local_context.update(self.context)
                return render(request, self.template, local_context)
            student.username = user_form.username
            student.email = user_form.email
            student.save()
            return HttpResponse(f'You have just created NEW student {student.username}')
        else:
            return HttpResponse('Sorry not now')

    def assign_course_to_user(self, user: CustomUser, course_name):
        course = Courses.objects.get(name=course_name)
        if getattr(user, self.user_role):
            user.courses.add(course)
        else:
            raise Courses.DoesNotExist
        user.save()
