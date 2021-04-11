from django.db import models


# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    distribution = models.BinaryField()  # tells wich day in week the course takes place eg. 0100 0001 = means only in sundaty and monday


class Exceptions(models.Model):
    name = models.CharField(max_length=20)  # choroba
    date = models.DateField()  # 12.1219978
    description = models.CharField(max_length=100)  # gruźlica nauczyciela plus srtaczka
    related_course = models.ForeignKey(Courses, on_delete=models.CASCADE)


class GeneralException(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    description = models.CharField(max_length=100)
