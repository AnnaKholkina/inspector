from django.db import models

class Unit(models.Model):
    unit_name = models.CharField(max_length=60, unique=True)
    status = models.CharField(max_length=5)

class Member(models.Model):
    name = models.CharField(max_length=200, unique=True)
    unit_name = models.CharField(max_length=60, null=True)
