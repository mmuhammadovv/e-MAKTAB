from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import file_size
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from .models import *

#users 
class Account(models.Model):
    type = models.CharField(max_length=55)

    def __str__(self):
        return self.type


class User(AbstractUser):
    age = models.CharField(max_length=2)
    place_of_living = models.CharField(max_length=55)
    is_admin= models.BooleanField('Is admin', default=False)
    is_teacher = models.BooleanField('Is Teacher', default=False)
    is_pupil = models.BooleanField('Is Pupil', default=False)
    type = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)


# contact
class Contact(models.Model):
    name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=13)
    email = models.EmailField()
    description = models.TextField()


    def __str__(self):
        return self.name
    


# lessons

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(upload_to='files/',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp4'])])