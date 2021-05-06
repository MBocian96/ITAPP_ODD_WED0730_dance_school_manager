import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication_module.managers import UserManager
from courses_module.models import Courses
from dance_school_manager.settings import IMAGES_ROOT

EMPLOYEE = 'employee'
TEACHER = 'teacher'
STUDENT = 'student'
UNKNOWN = 'unknown'


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to=IMAGES_ROOT, blank=True, default=None, null=True)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    # deposit = models.IntegerField(verbose_name="deposit of monet", max_length=2)

    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    courses = models.ManyToManyField(Courses, blank=True)

    objects = UserManager()

    def get_user_type(self) -> str:
        if self.is_employee:
            return EMPLOYEE
        elif self.is_teacher:
            return TEACHER
        elif self.is_student:
            return STUDENT
        else:
            return UNKNOWN

    def __str__(self):
        return f'{self.email}: {self.username}'

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def get_missed_courses(self):
        missed_course = MissedCourse.objects.get(related_course__id=self.id)
        return missed_course.related_course.all()

    def add_missing_course(self, related_course_id):
        # currently_ongoing_course = get_ongoing_course()
        course = Courses.objects.get(related_course_id)
        user = CustomUser.objects.get(self.id)

        missing_course = MissedCourse(date=datetime.time())
        missing_course.related_course = course
        missing_course.related_user = user
        missing_course.save()


class MissedCourse(models.Model):
    date = models.DateField()
    related_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    related_course = models.OneToOneField(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f'MissedCourse: {self.date}, {self.related_course}'
