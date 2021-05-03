from employee_module.views.employee_main_view import EmployeeView


class ManageTeachersView(EmployeeView):
    template = 'profiles/employee/teacher/manage_teachers_view.html'
    filter_arg = {'is_teacher': True}
