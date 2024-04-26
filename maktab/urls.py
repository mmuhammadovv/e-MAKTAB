from django.urls import path
from .views import *


urlpatterns = [
    # home 
    path("", home, name="home"),


    # user urls
    path("add_user", add_user, name="add_user"),
    path("login", login_function, name="login"),
    path('logout', logoutfunction , name='logout'),
    path("account", account, name="account"),
    path('user_delete/<str:pk>/',user_delete, name='user_delete'),
    path('user_update/<str:pk>/',user_update, name='user_update'),
    path("user/<int:pk>", user, name="user"),
    path("users", users, name="users"),


    # lesson urls
    path("add_lesson", add_lesson, name="add_lesson"),
    path('lesson/<int:pk>/', lesson, name='lesson'),
    path("lessons", lessons, name="lessons"),
    path('lesson_delete/<str:pk>/',lesson_delete, name='lesson_delete'),
    path('lesson_update/<str:pk>/',lesson_update, name='lesson_update'),
    path('stream/<int:pk>/', streaming_lesson, name='stream'),


    # contact and search urls
    path('contact', contact , name='contact'),
    path('search', search, name='search'),
]
