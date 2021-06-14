from django.contrib.auth.decorators import login_required
from django.urls import path

from client_module.views import ClientView, ClientSettingsView, AbandonCourse, CalendarView, ReportAbsenceView
from employee_module.urls import login_url

app_name = 'client_module'
urlpatterns = [
    path('', login_required(ClientView.as_view(), login_url=login_url), name='user_view'),
    path('settings/', login_required(ClientSettingsView.as_view(), login_url=login_url), name='user_settings_view'),
    path('abandon/<int:pk>', login_required(AbandonCourse, login_url=login_url), name='abandon_course_view'),
    path('calendar/', login_required(CalendarView.as_view(), login_url=login_url), name='calendar_view'),
    path('report_absence/', login_required(ReportAbsenceView.as_view(), login_url=login_url),
         name='report_absence_view'),
]
