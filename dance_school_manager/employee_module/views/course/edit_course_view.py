from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.forms.course.create_course_form import CreateCourseForm
from employee_module.views.base.manage_user_view import ManageUserView


class EditCourseView(ManageUserView):
    template = 'profiles/employee/course/edit_course_view.html'

    def get(self, request, course_id: int):
        course = get_object_or_404(Courses, id=course_id)
        students_attended_to_this_course: QuerySet = CustomUser.objects.filter(courses__id=course_id)

        course_form = CreateCourseForm(
            initial={'name': course.name,
                     'description': course.description,
                     'room': course.room,
                     'start_date': course.start_date,
                     'days': course.days,
                     'time': course.time,
                     'end_date': course.end_date,
                     })
        for i, student in enumerate(students_attended_to_this_course):
            course_form.initial.update({f'{i}_student': student.email})

        local_context = {'course_form': course_form,
                         'username': request.user.username,
                         'avatar': request.user.avatar,
                         }
        local_context.update(self.context)
        return render(request, self.template, local_context)

    def post(self, request, course_id: int):
        course_form = CreateCourseForm(request.POST) 
        local_context = {'course_form': course_form,
                         'username': request.user.username,
                         'avatar': request.user.avatar, }
        if course_form.is_valid():
            course = Courses.objects.get(id=course_id)
            emails_not_found = []
            for field in course_form.fields.keys():
                email = course_form.cleaned_data[field]
                if field.endswith('student') and email:
                    try:
                        self.assign_course_to_student_by(email=email, course=course)
                    except CustomUser.DoesNotExist:
                        emails_not_found.append(email)
            if emails_not_found:
                local_context.update({'emails_not_found': emails_not_found, })
                local_context.update(self.context)
                return render(request, self.template, local_context)
            course.room = course_form.cleaned_data['room']
            course.name = course_form.cleaned_data['name']
            course.time = course_form.cleaned_data['time']
            course.description = course_form.cleaned_data['description']
            course.start_date = course_form.cleaned_data['start_date']
            course.end_date = course_form.cleaned_data['end_date']
            course.days = course_form.cleaned_data['days']
            course.save()
            local_context.update({'warrning': f'You created course {str(course)}'})
            return render(request, self.template, local_context)
        else:
            local_context.update({'warrning': 'Course can not be created'})
            return render(request, self.template, local_context)

    @classmethod
    def assign_course_to_student_by(cls, email, course):
        user = CustomUser.objects.get(email=email)
        if user.is_student:
            user.courses.add(course)
        else:
            raise CustomUser.DoesNotExist
        user.save()
