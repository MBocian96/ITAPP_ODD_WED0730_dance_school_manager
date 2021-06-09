from django.db import models

from datetime import  datetime
from authentication_module.models import CustomUser
from courses_module.models import Courses

# Create your models here.
class Message(models.Model):
    #jak bedzie wiadomo ze to ten uzytkownik napisał ?
    #models.ForeignKey(User)
   # name = models.CharField(max_length=20)
    text = models.TextField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
   # ? related_student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=False)
    related_course = models.ForeignKey(Courses, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return f'Message: {self.text}, {self.date_created}, {self.related_course}'




