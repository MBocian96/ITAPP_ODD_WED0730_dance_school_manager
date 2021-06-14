from django.urls import path

from teacher_module.views.create_message import MessagePostView
from teacher_module.views.main_view import TeacherView
from teacher_module.views.school_courses import SchoolCoursesViews
from teacher_module.views.settings_view import SettingsViews
from teacher_module.views.view_courses import CoursesListViews
from teacher_module.views.calendar import CalendarViews
from teacher_module.views.course_page import CoursePageViews, CoursesViews

app_name = "teacher_module"

urlpatterns = [
    path('', TeacherView.as_view(), name='teacher_profile_view'),
    path('courses_list/', CoursesListViews.as_view(), name='courses_list_view'),
    path('settings/', SettingsViews.as_view(), name='settings_view'),
    path('calendar/', CalendarViews.as_view(), name='calendar_view'),
    path('courses/', CoursesViews.as_view(), name='courses_view'),
    path('certain_course/<int:course_id>/', CoursePageViews.as_view(), name='course_page_view'),
    path('certain_course/create_message/', MessagePostView.as_view(), name='create_message_view')
]
