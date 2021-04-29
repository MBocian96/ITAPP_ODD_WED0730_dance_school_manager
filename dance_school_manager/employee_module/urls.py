from django.urls import path

from employee_module.views.create_course_view import CreateCoursesViews
from employee_module.views.edit_course_view import EditCoursesViews
from employee_module.views.main_view import EmployeeView
from employee_module.views.manage_courses_view import ManageCoursesViews

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee_view'),
    path('manage_courses/', ManageCoursesViews.as_view(), name='manage_courses_view'),
    path('create_course/', CreateCoursesViews.as_view(), name='create_courses_view'),
    path('edit_course/<int:course_id>/', EditCoursesViews.as_view(), name='edit_courses_view'),
]
