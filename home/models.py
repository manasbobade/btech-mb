import email
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    problem=models.CharField(max_length=500,default="m")
    date=models.DateField()

    def __str__(self):
        return self.name 