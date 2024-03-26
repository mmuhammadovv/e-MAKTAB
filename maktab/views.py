from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def admin_account(request):
    return render(request, 'admin_account.html')

def teacher_account(request):
    return render(request, 'teacher_account.html')

def pupil_account(request):
    return render(request, 'pupil_account.html')

def pupils(request):
    return render(request, 'pupils.html')

def teachers(request):
    return render(request, 'teachers.html')

def lessons(request):
    return render(request, 'lessons.html')


def add_lesson(request):
    return render(request, 'add_lesson.html')


def add_teacher(request):
    return render(request, 'add_teacher.html')


def add_pupil(request):
    return render(request, 'add_pupil.html')


def login_function(request):
    return render(request, 'login.html')