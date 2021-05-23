from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from employee_module.forms.teacher.create_teacher_form import CreateTeacherForm
from employee_module.views.base.edit_user_view import EditUserView


class EditTeacherView(EditUserView):
    template = 'profiles/employee/teacher/edit_teacher_view.html'
    user_form = CreateTeacherForm
    user_role = 'is_teacher'
