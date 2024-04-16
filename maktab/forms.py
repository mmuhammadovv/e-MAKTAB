from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

# lesson form
class Lesson_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','description', 'image','file']
    



# user form
        


# login
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



# signup
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )



    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )



    age = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    place_of_living = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    
    
    

    class Meta:
        model = User
        fields = ('first_name','username', 'email', 'age', 'place_of_living', 'password1', 'password2', 'is_admin', 'is_teacher', 'is_pupil', 'type')

