from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('admin_account', admin_account, name='admin_account'),
    path('admin_account', teacher_account, name='teacher_account'),
    path('admin_account', pupil_account, name='pupil_account'),
    path('lessons', lessons, name='lessons'), 
    path('teachers', teachers, name='teachers'), 
    path('pupils', pupils, name='pupils'), 
    path('add_lesson', add_lesson, name='add_lesson'),
    path('add_teacher', add_teacher, name='add_teacher'),
    path('add_pupil', add_pupil, name='add_pupil'),
]