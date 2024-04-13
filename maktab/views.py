from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.http import StreamingHttpResponse
from django.contrib import messages
from .services import open_file
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    teachers = User.is_teacher
    return render(request, "base.html", {'teachers':teachers})

@login_required(login_url='login')
def account(request):
    all_lesson=Video.objects.all()
    return render(request, "account.html", {'all':all_lesson})

@login_required(login_url='login')
def pupils(request):
    return render(request, "pupils.html")

@login_required(login_url='login')
def teachers(request):
    teachers = User.objects.all()
    
    return render(request, "teachers.html", {'teachers':teachers})

@login_required(login_url='login')
def lessons(request):
    all_lesson=Video.objects.all()
    return render(request, "lessons.html",{"all":all_lesson})


@login_required(login_url='login')
def lesson(request, pk:int):
    lesson = get_object_or_404(Video, id=pk)
    return render(request, 'lesson.html', {'lesson':lesson})


def streaming_lesson(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        lessons = Video.objects.filter(title__contains = searched)

        return render(request, 'search_result.html', {'searched':searched, 'lessons':lessons})
    else:
        return render(request, 'search_result.html')


@login_required(login_url='login')
def add_lesson(request):
    if request.method == "POST":
        form=Lesson_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lessons')
    else:
        form=Lesson_form()
    return render(request, "add_lesson.html", {'form':form})

@login_required(login_url='login')
def add_user(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('account')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()

    return render(request, "add_user.html", {'form':form, 'msg':msg})



def login_function(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)    
            login(request, user)
            return redirect('home')
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form':form, 'msg':msg})


def logoutfunction(request):
    logout(request)
    return redirect('home')


def contact(request):

    if request.method=='POST':
        name = request.POST.get('fullname')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        description = request.POST.get('description')
        myquery = Contact(name=name, phonenumber=phonenumber, email=email, description=description)
        myquery.save()
        return redirect('/')


