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
    avatar = models.ImageField(upload_to=IMAGES_ROOT)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    courses = models.ManyToManyField(Courses)

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
