from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("account", account, name="account"),
    path("lessons", lessons, name="lessons"),
    path('search', search, name='search'),
    path("teachers", teachers, name="teachers"),
    path("pupils", pupils, name="pupils"),
    path("add_lesson", add_lesson, name="add_lesson"),
    path("add_user", add_user, name="add_user"),
    path("login", login_function, name="login"),
    path('logout', logoutfunction , name='logout'),
    path('contact', contact , name='contact'),
    path('stream/<int:pk>/', streaming_lesson, name='stream'),
    path('lesson/<int:pk>/', lesson, name='lesson'),

]
