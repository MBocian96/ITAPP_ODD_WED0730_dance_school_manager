from employee_module.forms.student.create_student_form import CreateStudentForm
from employee_module.views.base.create_user_view import CreateUserView


class CreateStudentView(CreateUserView):
    template = 'profiles/employee/student/edit_student_view.html'
    user_form = CreateStudentForm
    user_role = 'is_student'
