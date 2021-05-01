from django.urls import path

from client_module import views
from client_module.views import ClientView, ClientSettingsView, AbandonCourse

app_name = 'client_module'
urlpatterns = [
    path('', ClientView.as_view(), name='user_view'),
    path('settings/', ClientSettingsView.as_view(), name='user_settings_view'),
    path('abandon/<int:pk>', AbandonCourse, name='abandon_course_view'),
]
