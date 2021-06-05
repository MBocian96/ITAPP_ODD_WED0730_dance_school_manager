# Generated by Django 3.2 on 2021-06-05 14:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('room', models.IntegerField(default=0)),
                ('start_date', models.DateField(default=datetime.date(2021, 6, 5))),
                ('days', models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], default='Monday', max_length=70)),
                ('time', models.TimeField(default=datetime.time(14, 28, 44, 698357))),
                ('end_date', models.DateField(default=datetime.date(2021, 7, 31))),
            ],
        ),
        migrations.CreateModel(
            name='GeneralException',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exceptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('related_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_module.courses')),
            ],
        ),
    ]
