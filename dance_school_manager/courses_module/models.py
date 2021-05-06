from datetime import datetime, timedelta
from time import time

from django.db import models

from courses_module.utils import get_day_number_by
from dance_school_manager.settings import HOUR_FORMAT

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class Courses(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    start_date = models.DateField(default=datetime.now().date())
    days = models.CharField(choices=DAYS_OF_WEEK, default='Monday', max_length=70)
    time = models.TimeField(default=datetime.now().time())

    end_date = models.DateTimeField(default=datetime.now().date() + timedelta(weeks=8))

    def __str__(self):
        return f'Course {self.name}: {self.description}'

    def is_ongoing(self):
        current_time: time = datetime.now()
        if self.start_date <= current_time.date() < self.end_date:
            if get_day_number_by(self.days) == current_time.weekday():
                if self.time.strftime(HOUR_FORMAT) == current_time.time().strftime(HOUR_FORMAT):
                    return True
        return False


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
