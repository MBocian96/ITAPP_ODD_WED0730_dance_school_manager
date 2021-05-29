from django.urls import path

from client_module import views
from client_module.views import ClientView, ClientSettingsView, AbandonCourse, CallendarView

app_name = 'client_module'
urlpatterns = [
    path('', ClientView.as_view(), name='user_view'),
    path('settings/', ClientSettingsView.as_view(), name='user_settings_view'),
    path('abandon/<int:pk>', AbandonCourse, name='abandon_course_view'),
    path('callendar/', CallendarView.as_view(), name='callendar_view'),
]
