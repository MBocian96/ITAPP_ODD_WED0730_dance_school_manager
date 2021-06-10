from django.db import models

from authentication_module.models import CustomUser
from courses_module.models import Courses

# Create your models here.
class Message(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField(max_length=600)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=False)
    related_course = models.ForeignKey(Courses, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return f'Message:  {self.title}, {self.text}, {self.date_created}'




