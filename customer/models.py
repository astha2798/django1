from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class customer(models.Model):
	username=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
