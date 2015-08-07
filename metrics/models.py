from django.db import models

# Create your models here.

class Year(models.Model):
    name = models.CharField(max_length = 255)
    number = models.IntegerField()

class Party(models.Model):
    name = models.CharField(max_length = 255)
    number = models.IntegerField()

class County(models.Model):
    name = models.CharField(max_length = 255)
    number = models.IntegerField()

