# Generated by Django 3.2.5 on 2021-09-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rollcall', '0017_auto_20210902_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsignin',
            name='ClassroomId',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentsignin',
            name='UserId',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='ClassroomId',
            field=models.TextField(blank=True),
        ),
    ]
