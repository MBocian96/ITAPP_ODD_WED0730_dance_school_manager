from datetime import timedelta
from typing import List

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator

from authentication_module.models import CustomUser, MissedCourse
from courses_module.models import Courses
from employee_module.forms.student.create_student_form import CreateStudentForm
from employee_module.views.base.edit_user_view import EditUserView


class EditStudentView(EditUserView):
    template = 'profiles/employee/student/edit_student_view.html'
    user_form = CreateStudentForm
    user_role = 'is_student'

    def get(self, request, user_id: int):
        student = get_object_or_404(CustomUser, id=user_id)
        absences_to_show: List[Courses] = student.get_absences()
        ongoing_courses = student.get_ongoing_courses(timedelta(minutes=15))
        marked_as_present = get_marked_as_present(ongoing_courses, student.get_aboslut_absences())
        date = timezone.now().date()
        additional_context = {'ongoing_courses': ongoing_courses,
                              'deposit': student.deposit,
                              'student': student,
                              'absences': absences_to_show,
                              'marked_as_present': marked_as_present,
                              'date': date,
                              }
        return super(EditStudentView, self).get(request, user_id, additional_context)


def set_present(request, date, user_id, course_id):
    missed_course = MissedCourse.objects.filter(date=date, related_student__id=user_id, related_course__id=course_id)
    missed_course.delete()
    return redirect(f'/employee/edit_student/{user_id}/')


def get_marked_as_present(ongoing, absences):
    result = []
    for course in ongoing:
        if course not in absences:
            result.append(course)
    return result


def substract_deposit(student):  # run 15min before course end
    ongoing_courses = student.get_ongoing_courses(timedelta(minutes=0))
    absences = student.get_aboslut_absences()
    for course in ongoing_courses:
        if course in absences:
            student.deposit -= 15
