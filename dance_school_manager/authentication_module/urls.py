from django.urls import path, include

from authentication_module.views import StudentSignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sign_up/student/', StudentSignUpView.as_view(), name='student_signup'),
]
