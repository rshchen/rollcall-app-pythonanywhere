# Generated by Django 3.2.5 on 2021-08-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rollcall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroomid', models.CharField(max_length=30)),
                ('namelist', models.TextField()),
            ],
        ),
    ]
