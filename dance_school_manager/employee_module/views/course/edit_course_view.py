from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.forms.course.create_course_form import CreateCourseForm
from employee_module.views.employee_main_view import EmployeeView


class EditCourseView(EmployeeView):
    template_name = 'profiles/employee/course/edit_course_view.html'

    def get(self, request, course_id: int):
        course = get_object_or_404(Courses, id=course_id)
        students_attended_to_this_course = CustomUser.objects.filter(courses__id=course_id)

        course_form = CreateCourseForm(initial={'name': course.name, 'description': course.description})
        for i, student in enumerate(students_attended_to_this_course):
            course_form.initial.update({f'{i}_student': student.email})
        local_context = {'course_form': course_form,
                         'username': request.user.username,
                         'avatar': request.user.avatar,
                         }
        local_context.update(self.context)
        return render(request, self.template_name, local_context)

    def post(self, request, course_id: int):
        course_form = CreateCourseForm(request.POST)
        if course_form.is_valid():
            course = Courses.objects.get(id=course_id)
            emails_not_found = []
            for student in course_form.fields.keys():
                email = course_form.cleaned_data[student]
                if student.endswith('student') and email:
                    try:
                        self.assign_course_to_student_by(email=email, course=course)
                    except CustomUser.DoesNotExist:
                        emails_not_found.append(email)
            if emails_not_found:
                local_context = {'course_form': course_form,
                                 'emails_not_found': emails_not_found,
                                 'username': request.user.username,
                                 'avatar': request.user.avatar, }
                local_context.update(self.context)
                return render(request, self.template_name, local_context)
            course.save()
            return HttpResponse(f'You created course {str(course)}, and proper')
        else:
            return HttpResponse('Sorry not now')

    @classmethod
    def assign_course_to_student_by(cls, email, course):
        user = CustomUser.objects.get(email=email)
        user.save()
        course.save()
        if user.is_student:
            user.courses.add(course)
        else:
            raise CustomUser.DoesNotExist
