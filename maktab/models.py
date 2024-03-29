from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import file_size


#users 

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PUPIL = "PUPIL", "Pupil"
        TEACHER = "TEACHER", "Teacher"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class PupilManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PUPIL)


class Pupil(User):
    base_role = User.Role.PUPIL

    pupil = PupilManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Pupil"


@receiver(post_save, sender=Pupil)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        PupilProfile.objects.create(user=instance)


class PupilProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pupil_id = models.IntegerField(null=True, blank=True)


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)


class Teacher(User):
    base_role = User.Role.TEACHER

    teacher = TeacherManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Teacher"


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "TEACHER":
        TeacherProfile.objects.create(user=instance)




# lessons 
class Lesson(models.Model):
    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    video = models.FileField(upload_to='lesson/%y', validators=[file_size])


    def __str__(self):
        return self.topic
    


# contact
class Contact(models.Model):
    name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=13)
    email = models.EmailField()
    description = models.TextField()


    def __str__(self):
        return self.name