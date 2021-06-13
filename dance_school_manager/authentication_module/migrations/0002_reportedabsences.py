# Generated by Django 3.2 on 2021-06-11 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_module', '0002_auto_20210611_1631'),
        ('authentication_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportedAbsences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('related_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_module.courses')),
                ('related_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]