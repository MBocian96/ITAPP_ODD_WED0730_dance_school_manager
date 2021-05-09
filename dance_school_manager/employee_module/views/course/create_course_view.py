from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.forms.course.create_course_form import CreateCourseForm
from employee_module.views.base.manage_user_view import ManageUserView


class CreateCourseView(ManageUserView):
    template = 'profiles/employee/course/create_course_view.html'

    @method_decorator(login_required)
    def get(self, request):
        course_form = CreateCourseForm()
        local_context = {'course_form': course_form}
        local_context.update(self.context)
        return render(request, self.template, local_context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        course_form = CreateCourseForm(request.POST)
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
                local_context = {'course_form': course_form,
                                 'emails_not_found': emails_not_found,
                                 'username': request.user.username,
                                 'avatar': request.user.avatar, }
                local_context.update(self.context)
                return render(request, self.template, local_context)
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
        user.save()
