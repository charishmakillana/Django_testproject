from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Model


class Validation(models.Model):
    name = models.CharField(max_length=20, blank=False,null=False)
    URL = models.URLField()

    phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Pictures(models.Model):
    pics = models.ImageField(upload_to='img/')