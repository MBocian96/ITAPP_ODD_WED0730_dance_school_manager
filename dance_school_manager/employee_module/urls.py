from django.urls import path, register_converter

from authentication_module.models import set_absance
from employee_module import url_converter
from employee_module.views.course.create_course_view import CreateCourseView
from employee_module.views.course.edit_course_view import EditCourseView
from employee_module.views.course.manage_courses_view import ManageCoursesView
from employee_module.views.default_employee_view import EmployeeHomeView
from employee_module.views.student.create_student_view import CreateStudentView
from employee_module.views.student.edit_student_view import EditStudentView, set_present
from employee_module.views.student.manage_student_view import ManageStudentsView
from employee_module.views.teacher.create_teacher_view import CreateTeacherView
from employee_module.views.teacher.edit_teacher_view import EditTeacherView
from employee_module.views.teacher.manage_teachers_view import ManageTeachersView

register_converter(url_converter.DateTimeConverter, 'date')

app_name = 'employee_module'
urlpatterns = [
    path('', EmployeeHomeView.as_view(), name='employee_home_view'),

    # courses
    path('create_course/', CreateCourseView.as_view(), name='create_course_view'),
    path('manage_courses/', ManageCoursesView.as_view(), name='manage_courses_view'),
    path('edit_course/<int:course_id>/', EditCourseView.as_view(), name='edit_course_view'),

    # teachers
    path('manage_teachers/', ManageTeachersView.as_view(), name='manage_teachers_view'),
    path('create_teachers/', CreateTeacherView.as_view(), name='create_teacher_view'),
    path('edit_teacher/<int:user_id>/', EditTeacherView.as_view(), name='edit_teacher_view'),

    # students
    path('manage_students/', ManageStudentsView.as_view(), name='manage_students_view'),
    path('create_student/', CreateStudentView.as_view(), name='create_student_view'),
    path('edit_student/<int:user_id>/', EditStudentView.as_view(), name='edit_student_view'),

    # mechanisms
    path('set_absances/', set_absance, name='set_absance'),
    path('set_present/<date:date>/<int:user_id>/<int:course_id>/', set_present, name='set_present')
]
