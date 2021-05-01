from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from authentication_module.models import CustomUser
from courses_module.models import Courses
from employee_module.forms.create_course_form import CreateCourseForm


class EditCoursesViews(View):
    template_name = 'profiles/employee/edit_course_view.html'

    def get(self, request, course_id: int):
        course = get_object_or_404(Courses, id=course_id) #pobieram konkretny kurs o podanym id jesli go nie ma to renderuje się strona z 404

        students_attended_to_this_course = CustomUser.objects.filter(courses__id=course_id) #
        # w polu customUser.courses są cursy na które ucześcza # relacja
        # pobieram userów którzy w tym polu mają kurs o id równym id kursy który teraz edytuje

        course_form = CreateCourseForm(initial={'name': course.name, 'description': course.description})
        # wpisuje do formularza wczesnije wyciągniete dane

        for i, student in enumerate(students_attended_to_this_course):
            course_form.initial.update({f'{i}_student': student.email})
            return render(request, self.template_name, {'course_form': course_form})
        # chodze po wsyzstkich studentach i updateuje po kolei pola ich emailem.


    def post(self, request, course_id: int, *args, **kwargs):
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
                return render(request, self.template_name,
                              {'course_form': course_form, 'emails_not_found': emails_not_found})
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
