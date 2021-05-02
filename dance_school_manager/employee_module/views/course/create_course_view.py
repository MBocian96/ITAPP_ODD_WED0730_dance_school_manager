from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.forms.course.create_course_form import CreateCourseForm


class CreateCourseView(View):
    template_name = 'profiles/employee/course/create_course_view.html'
    context = {'course': 'course',
               'manage_students': 'manage_students',
               'teacher': 'teacher'
               }

    def get(self, request):
        course_form = CreateCourseForm()
        local_context = {'course_form': course_form}
        local_context.update(self.context)
        return render(request, self.template_name, local_context)

    def post(self, request, *args, **kwargs):
        course_form = CreateCourseForm(request.POST)
        course = None
        if course_form.is_valid():
            name = course_form.cleaned_data['name']
            description = course_form.cleaned_data['description']
            course = Courses(name=name, description=description)
            emails_not_found = []

            for student in course_form.fields.keys():
                email = course_form.cleaned_data[student]
                if student.endswith('student') and email:
                    try:
                        self.assign_course_to_student_by(email=email, course=course)
                    except CustomUser.DoesNotExist:
                        emails_not_found.append(email)
            if emails_not_found:
                return render(request, self.template_name,
                              {'course_form': course_form, 'emails_not_found': emails_not_found})
            course.save()
            return HttpResponse(f'You created course {str(course)}, and proper')
        else:
            return HttpResponse('Sorry not now')

    @classmethod
    def assign_course_to_student_by(cls, email, course):
        user = CustomUser.objects.get(email=email)
        if user.is_student:
            user.courses.add(course)
        else:
            raise CustomUser.DoesNotExist
