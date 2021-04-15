from django.urls import path

from employee_module.views.main_view import EmployeeView
from employee_module.views.manage_courses_view import ManageCoursesViews

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee_view'),
    path('', ManageCoursesViews.as_view(), name='manage_courses_view'),
]
