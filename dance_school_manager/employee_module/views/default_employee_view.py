from django.shortcuts import render

from employee_module.views.base.manage_user_view import ManageUserView


class EmployeeHomeView(ManageUserView):
    template = 'profiles/employee/employee_home_view.html'

    def get(self, request):
        local_context = self.get_default_context(request)
        return render(request, self.template, local_context)

