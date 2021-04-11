from django.contrib import admin

# Register your models here.
from courses_module.models import Courses, Exceptions, GeneralException

admin.site.register(Courses)
admin.site.register(Exceptions)
admin.site.register(GeneralException)
