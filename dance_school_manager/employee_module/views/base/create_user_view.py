from typing import Callable

from django.shortcuts import render

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.views.base.manage_user_view import ManageUserView


class CreateUserView(ManageUserView):
    template = '/'
    user_form: Callable
    user_role = 'is_'

    def get(self, request):
        user_form = self.user_form()
        local_context = {'user_form': user_form}
        local_context.update(self.context)
        return render(request, self.template, local_context)

    def post(self, request):
        user_form = self.user_form(request.POST)
        local_context = {'user_form': user_form}
        local_context.update(self.context)
        if user_form.is_valid():
            name = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            student = CustomUser(username=name, email=email, password=password, _teacher=True)
            courses_not_found = []
            for field in user_form.fields.keys():
                if field.endswith('course'):
                    course_name = user_form.cleaned_data[field]
                    try:
                        self.assign_course_to_user(user=student, course_name=course_name)
                    except Courses.DoesNotExist:
                        courses_not_found.append(course_name)
            if courses_not_found:
                local_context.update({'courses_not_found': courses_not_found})
                return render(request, self.template, local_context)
            student.username = user_form.username
            student.email = user_form.email
            student.save()
            local_context.update({'warrning': f'You created student{str(student)}'})
            return render(request, self.template, local_context)
        else:
            local_context.update({'warrning': 'User can not be created'})
            return render(request, self.template, local_context)

    def assign_course_to_user(self, user: CustomUser, course_name):
        course = Courses.objects.get(name=course_name)
        if getattr(user, self.user_role):
            user.courses.add(course)
        else:
            raise Courses.DoesNotExist
        user.save()
