from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=25)


class User(models.Model):
    permissions = models.ManyToManyField(Group)
    login = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    logo = models.CharField(max_length=25)



