# Generated by Django 3.2 on 2021-06-10 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='end_date',
            field=models.DateField(default=datetime.date(2021, 8, 5)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 6, 10)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='time',
            field=models.TimeField(default=datetime.time(21, 3, 19, 274641)),
        ),
    ]