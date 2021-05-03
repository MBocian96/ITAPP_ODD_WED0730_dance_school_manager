from django.urls import path

from employee_module.views.course.create_course_view import CreateCourseView
from employee_module.views.course.edit_course_view import EditCourseView
from employee_module.views.course.manage_courses_view import ManageCoursesView
from employee_module.views.employee_main_view import EmployeeView
from employee_module.views.student.edit_student_view import EditStudentView
from employee_module.views.student.manage_student_view import ManageStudentsView
from employee_module.views.teacher.edit_teacher_view import EditTeacherView
from employee_module.views.teacher.manage_teachers_view import ManageTeachersView

app_name = 'employee_module'
urlpatterns = [
    path('', EmployeeView.as_view(), name='employee_view'),

    # courses
    path('create_course/', CreateCourseView.as_view(), name='create_course_view'),
    path('manage_courses/', ManageCoursesView.as_view(), name='manage_courses_view'),
    path('edit_course/<int:course_id>/', EditCourseView.as_view(), name='edit_course_view'),

    # teachers
    path('manage_teachers/', ManageTeachersView.as_view(), name='manage_teachers_view'),
    path('edit_teacher/<int:user_id>/', EditTeacherView.as_view(), name='edit_teacher_view'),

    # students
    path('manage_students/', ManageStudentsView.as_view(), name='manage_students_view'),
    path('edit_student/<int:user_id>/', EditStudentView.as_view(), name='edit_student_view'),
]
