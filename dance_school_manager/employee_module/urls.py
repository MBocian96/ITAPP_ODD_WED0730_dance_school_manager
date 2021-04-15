from django.urls import path

from employee_module.views import EmployeeView

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee_view'),
]
