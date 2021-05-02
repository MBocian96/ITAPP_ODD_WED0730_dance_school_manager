from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.forms.teacher.create_teacher_form import CreateTeacherForm
from employee_module.views.teacher.create_teacher_view import CreateTeacherView


class EditTeacherView(CreateTeacherView):
    template = 'profiles/employee/teacher/edit_teacher_view.html'

    @method_decorator(login_required)
    def get(self, request, teacher_id: int):
        teacher = get_object_or_404(CustomUser, id=teacher_id)
        courses: QuerySet = teacher.courses.all()

        teacher_form = CreateTeacherForm(initial={'username': teacher.username, 'email': teacher.email})
        for i, course in enumerate(courses):
            print({f'{i}_course': course.name})
            teacher_form.initial.update({f'{i}_course': course.name})

        local_context = {'teacher_form': teacher_form,
                         'username': request.user.username,
                         'avatar': request.user.avatar,
                         }
        local_context.update(self.context)

        return render(request, self.template, local_context)

    @method_decorator(login_required())
    def post(self, request, teacher_id: int, *args, **kwargs):
        teacher_form = CreateTeacherForm(request.POST)
        teacher = get_object_or_404(CustomUser, id=teacher_id)
        if teacher_form.is_valid():
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
            return HttpResponse(f'You have just updated teacher {teacher.username}')
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
