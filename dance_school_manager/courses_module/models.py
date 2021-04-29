from django.db import models


# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    # start_date = models.DateField()
    # end_date = models.DateField()
    # distribution = models.BinaryField()  # tells wich day in week the course takes place eg. 0100 0001 = means only in sundaty and monday

    def __str__(self):
        return f'Course {self.name}: {self.description}'


class Exceptions(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    description = models.CharField(max_length=100)
    related_course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f'Exception: {self.name} : {self.description}'


class GeneralException(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'GeneralException: {self.name} : {self.description}'
