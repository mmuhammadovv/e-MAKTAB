from .models import *
from django import forms


class Lesson_form(forms.ModelForm):
    class Meta:
        model=Lesson
        fields=("topic","description", "video")