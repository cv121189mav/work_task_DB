# Generated by Django 2.2.3 on 2019-07-22 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='permissions',
        ),
        migrations.AddField(
            model_name='user',
            name='permissions',
            field=models.ManyToManyField(to='work_project.Group'),
        ),
    ]
