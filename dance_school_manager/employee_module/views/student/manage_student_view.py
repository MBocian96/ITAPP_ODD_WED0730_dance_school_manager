from employee_module.views.employee_main_view import EmployeeView


class ManageStudentsView(EmployeeView):
    template = 'profiles/employee/student/manage_student_view.html'
    filter_arg = {'is_student': True}
