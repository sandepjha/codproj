from django.db import models
# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=55)
    mobile = models.CharField(max_length=10,unique=True)
    email = models.EmailField(max_length=105)
    password = models.CharField(max_length=40)

