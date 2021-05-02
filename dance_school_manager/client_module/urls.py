from django.urls import path

from client_module.views import ClientView, ClientSettingsView

urlpatterns = [
    path('', ClientView.as_view(), name='user_view'),
    path('settings/', ClientSettingsView.as_view(), name='user_settings_view'),
]
