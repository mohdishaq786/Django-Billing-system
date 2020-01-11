from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentname = models.CharField(max_length=100,default='')
    Enrollmentno = models.CharField(max_length=100,default='0')
    billno = models.CharField(max_length=100,default='')
    cousre = models.CharField(max_length=100,default='')
    branch = models.CharField(max_length=100,default='')
    phoneno = models.CharField(max_length=10,default='')
    feestatus = models.CharField(max_length=10,default='')