from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator

from authentication_module.models import CustomUser, MissedCourse
from employee_module.forms.student.create_student_form import CreateStudentForm
from employee_module.views.base.edit_user_view import EditUserView


class EditStudentView(EditUserView):
    template = 'profiles/employee/student/edit_student_view.html'
    user_form = CreateStudentForm
    user_role = 'is_student'

    @method_decorator(login_required)
    def get(self, request, user_id: int):
        student = get_object_or_404(CustomUser, id=user_id)
        ongoing_courses = student.get_ongoing_courses(timedelta(minutes=15))
        additional_context = {'ongoing_courses': ongoing_courses[0], 'student': student}
        return super(EditStudentView, self).get(request, user_id, additional_context)


def set_present(request, user_id, course_id):
    missed_course = MissedCourse.objects.filter(related_student__id=user_id, related_course__id=course_id)
    missed_course.delete()
    return redirect(f'/employee/edit_student/{user_id}/')
