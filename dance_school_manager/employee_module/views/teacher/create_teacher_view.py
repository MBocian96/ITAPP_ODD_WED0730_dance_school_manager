from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.forms.teacher.create_teacher_form import CreateTeacherForm
from employee_module.views.employee_main_view import EmployeeView


class CreateTeacherView(EmployeeView):
    template = 'profiles/employee/teacher/edit_teacher_view.html'

    @method_decorator(login_required)
    def get(self, request):
        course_form = CreateTeacherForm()
        local_context = {'course_form': course_form}
        local_context.update(self.context)
        return render(request, self.template, local_context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        teacher_form = CreateTeacherForm(request.POST)
        if teacher_form.is_valid():
            name = teacher_form.cleaned_data['username']
            email = teacher_form.cleaned_data['email']
            teacher = CustomUser(username=name, email=email, is_teacher=True)
            courses_not_found = []
            for field in teacher_form.fields.keys():
                if field.endswith('course'):
                    course_name = teacher_form.cleaned_data[field]
                    try:
                        self.assign_course_to_user(user=teacher, course_name=course_name)
                    except Courses.DoesNotExist:
                        courses_not_found.append(course_name)
            if courses_not_found:
                local_context = {'teacher_form': teacher_form, 'courses_not_found': courses_not_found}
                local_context.update(self.context)
                return render(request, self.template, local_context)
            teacher.username = teacher_form.username
            teacher.email = teacher_form.email
            teacher.save()
            return HttpResponse(f'You have just created NEW teacher {teacher.username}')
        else:
            return HttpResponse('Sorry not now')

    @classmethod
    def assign_course_to_user(cls, user: CustomUser, course_name):
        course = Courses.objects.get(name=course_name)
        if user.is_teacher:
            user.courses.add(course)
        else:
            raise Courses.DoesNotExist
        user.save()
