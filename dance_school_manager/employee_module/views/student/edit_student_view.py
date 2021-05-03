from employee_module.forms.student.create_student_form import CreateStudentForm
from employee_module.views.base.edit_user_view import EditUserView


class EditStudentView(EditUserView):
    template = 'profiles/employee/student/edit_student_view.html'
    user_form = CreateStudentForm
    user_role = 'is_student'
