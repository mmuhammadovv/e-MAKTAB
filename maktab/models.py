from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import file_size
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from .models import *

#user models
class AccountType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class User(AbstractUser):
    type = models.ForeignKey(AccountType, related_name='users', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    age = models.CharField(max_length=2)
    place_of_living = models.CharField(max_length=55)
    is_admin= models.BooleanField('Is admin', default=False)
    is_teacher = models.BooleanField('Is Teacher', default=False)
    is_pupil = models.BooleanField('Is Pupil', default=False)


    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users_image/')

    def __str__(self):
        return f'{self.user.username} Profile'




# contact model
class Contact(models.Model):
    name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=13)
    email = models.EmailField()
    description = models.TextField()


    def __str__(self):
        return self.name
    


# lesson model
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(upload_to='files/',
                                  validators=[FileExtensionValidator(allowed_extensions=['mp4'])])