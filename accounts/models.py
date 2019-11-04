from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    injuries = models.CharField(max_length=50, blank = False, default="")
    mobile = models.CharField(max_length=50, blank=False, default="")