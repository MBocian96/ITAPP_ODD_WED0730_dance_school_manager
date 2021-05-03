from django.shortcuts import render

from authentication_module.models import CustomUser
from employee_module.views.base.manage_user_view import ManageUserView


class EmployeeHomeView(ManageUserView):
    template = 'profiles/employee/employee_home_view.html'

    def get(self, request):
        local_context = self.get_default_context(request)
        return render(request, self.template, local_context)

    def post(self, request):
        searched = request.POST['searched']
        result = CustomUser.objects.filter(username__contains=searched, is_student=False)
        local_context = self.get_default_context(request)
        local_context.update({'searched': searched,
                              'result': result
                              })
        return render(request, self.template, local_context)


