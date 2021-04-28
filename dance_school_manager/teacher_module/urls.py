from django.urls import path

from teacher_module.views.main_view import TeacherView


urlpatterns = [
    path('', TeacherView.as_view(), name='teacher_view'),

]
