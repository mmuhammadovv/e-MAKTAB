from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


# User forms
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'age', 'place_of_living', 'type','password1', 'password2', 'is_admin', 'is_teacher', 'is_pupil']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'age', 'place_of_living', 'type','is_admin', 'is_teacher', 'is_pupil']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'image']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']





# lesson form
class Lesson_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','description', 'image','file']
    

