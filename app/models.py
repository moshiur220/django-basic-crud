from django.db import models

# Create your models here.


class Student(models.Model):
    stname = models.CharField(max_length=70)
    stemail = models.CharField(max_length=70)
    stdep = models.CharField(max_length=50)
