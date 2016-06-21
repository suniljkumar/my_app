from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
class status(models.Model):
	name=models.CharField(max_length=200)
	mail=models.CharField(max_length=200)




# Create your models here.
