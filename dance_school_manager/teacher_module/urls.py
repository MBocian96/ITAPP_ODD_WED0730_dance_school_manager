from django.urls import path

from teacher_module.views.main_view import TeacherView
from teacher_module.views.school_courses import SchoolCoursesViews
from teacher_module.views.settings import SettingsViews
from teacher_module.views.view_courses import CoursesListViews
app_name= "teacher_module"

urlpatterns = [
    path('', TeacherView.as_view(), name='teacher_profile_view'),
    path('courses_list/', CoursesListViews.as_view(), name='courses_list_view'),
    path('settings/', SettingsViews.as_view(), name='settings_view'),
   # path('school_courses', SchoolCoursesViews.as_view(), name='school_courses_view'),
]