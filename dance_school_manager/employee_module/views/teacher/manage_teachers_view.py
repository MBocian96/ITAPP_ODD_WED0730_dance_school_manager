from employee_module.views.base.manage_user_view import ManageUserView


class ManageTeachersView(ManageUserView):
    template = 'profiles/employee/teacher/manage_teachers_view.html'
    filter_arg = {'is_teacher': True}
