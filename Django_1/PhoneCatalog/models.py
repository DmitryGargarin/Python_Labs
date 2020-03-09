from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    Name = models.CharField(max_length=255)
    RegDate = models.DateTimeField()
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=30)
