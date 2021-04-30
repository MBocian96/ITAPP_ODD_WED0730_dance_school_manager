from django.urls import path

from client_module.views import UserView, UserSettingsView
from employee_module.views.main_view import EmployeeView
from employee_module.views.manage_courses_view import ManageCoursesViews

urlpatterns = [
    path('', UserView.as_view(), name='user_view'),
    path('', UserSettingsView.as_view(), name='user_settings_view'),
]