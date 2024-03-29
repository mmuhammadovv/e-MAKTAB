from .models import *
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, "base.html")


def admin_account(request):
    return render(request, "admin_account.html")


def teacher_account(request):
    return render(request, "teacher_account.html")


def pupil_account(request):
    return render(request, "pupil_account.html")


def pupils(request):
    return render(request, "pupils.html")


def teachers(request):
    return render(request, "teachers.html")


def lessons(request):
    all_lesson=Lesson.objects.all()

    return render(request, "lessons.html",{"all":all_lesson})


def add_lesson(request):
    if request.method == "POST":
        form=Lesson_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lessons')
    else:
        form=Lesson_form()
    return render(request, "add_lesson.html", {'form':form})


def add_teacher(request):
    return render(request, "add_teacher.html")


def add_pupil(request): 
    return render(request, "add_pupil.html")


def login_function(request):
    return render(request, "login.html")



def contact(request):

    if request.method=='POST':
        name = request.POST.get('fullname')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        description = request.POST.get('description')
        myquery = Contact(name=name, phonenumber=phonenumber, email=email, description=description)
        myquery.save()
        return redirect('/')


