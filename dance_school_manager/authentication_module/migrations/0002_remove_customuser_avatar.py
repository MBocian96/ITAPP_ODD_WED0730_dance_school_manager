# Generated by Django 3.2 on 2021-05-01 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='avatar',
        ),
    ]
