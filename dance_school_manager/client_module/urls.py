from django.urls import path

from client_module.views import ClientView, ClientSettingsView
from employee_module.views.main_view import EmployeeView
from employee_module.views.manage_courses_view import ManageCoursesViews

urlpatterns = [
    path('', ClientView.as_view(), name='user_view'),
    path('settings', ClientSettingsView.as_view(), name='user_settings_view'),
]