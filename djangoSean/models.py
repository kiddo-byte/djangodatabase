from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, default='Kenya')
    phone = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default='Nairobi')


def __str__(self):
    return self.name
