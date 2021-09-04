# Generated by Django 3.2.5 on 2021-09-02 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rollcall', '0009_auto_20210902_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsignin',
            name='ClassroomId',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsignin',
            name='UserId',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='ClassroomId',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
