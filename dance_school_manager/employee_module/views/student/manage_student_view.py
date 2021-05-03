from employee_module.views.base.manage_user_view import ManageUserView


class ManageStudentsView(ManageUserView):
    template = 'profiles/employee/student/manage_student_view.html'
    filter_arg = {'is_student': True}
