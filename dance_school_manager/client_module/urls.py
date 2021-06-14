from django.urls import path

from client_module import views
from client_module.views import ClientView, ClientSettingsView, AbandonCourse, CalendarView, ReportAbsenceView

app_name = 'client_module'
urlpatterns = [
    path('', ClientView.as_view(), name='user_view'),
    path('settings/', ClientSettingsView.as_view(), name='user_settings_view'),
    path('abandon/<int:pk>', AbandonCourse, name='abandon_course_view'),
    path('calendar/', CalendarView.as_view(), name='calendar_view'),
    path('report_absence/', ReportAbsenceView.as_view(), name='report_absence_view'),
]
