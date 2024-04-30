from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.http import StreamingHttpResponse
from django.contrib import messages
from .services import open_file
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# base
def home(request ):
    lessons = Video.objects.count()
    teachers = User.objects.filter(type='1').count()
    pupils = User.objects.filter(type='2').count()

    return render(request, "base.html", {'lessons':lessons, 'teachers':teachers, 'pupils':pupils})




# user functions
def account(request):
    if request.method == 'POST':
        form = UserImageUpdateForm(request.POST, request.FILES ,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('account')
        else :
            messages.info(request, 'Something went wrong!')
            return redirect('account')

    else:
        form = UserImageUpdateForm(instance=request.user)

    context = {
        'form':form
    }

    return render(request, "account.html",context )

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        lessons = Video.objects.filter(title__contains = searched)

        return render(request, 'search_result.html', {'searched':searched, 'lessons':lessons})
    else:
        return render(request, 'search_result.html')

@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            messages.info(request, 'User added succesfully!')
            return redirect('users')
        else :
            messages.info(request, 'Something went wrong!')
            return redirect('users')
    else:
        form = SignUpForm()

    return render(request, "add_user.html", {'form':form})

def user_update(request, pk):

        user = User.objects.get(pk=pk)
        form = UserUpdateForm(instance=user)
        if request.method == 'POST':
                form = UserUpdateForm(request.POST, instance=user)
                if form.is_valid():
                    form.save()
                    messages.info(request, 'User updated succesfully!')
                    return redirect('users')
                else :
                    messages.info(request, 'Something went wrong!')
                    return redirect('users')
            

        context = {'form':form}
        return render(request, 'user_update.html', context)

def user_delete(request, pk):
    user = User.objects.get(pk=pk)

    context = {'user':user}

    if request.method == 'POST':
        user.delete()
        messages.info(request, 'User deleted succesfully!')
        return redirect('users')
    

    return render(request, 'user_delete.html', context)

@login_required(login_url='login')
def users(request):
    types = AccountType.objects.all()
    users = User.objects.all()

    active_type = request.GET.get('type', '')

    if active_type:
        users = users.filter(type__slug=active_type)


    context = {
        'users':users,
        'types':types,
        'active_type':active_type
    }

    return render(request, "users.html", context)

def user(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, "user.html", {'user':user})




# lesson functions
@login_required(login_url='login')
def add_lesson(request):
    if request.method == "POST":
        form=Lesson_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Lesson added succesfully!')
            return redirect('lessons')
        else :
            messages.info(request, 'Something went wrong!')
            return redirect('lessons')
    else:
        form=Lesson_form()
    return render(request, "add_lesson.html", {'form':form})

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

def lesson_delete(request, pk):
    lesson = Video.objects.get(pk=pk)

    context = {'lesson':lesson}

    if request.method == 'POST':
        lesson.delete()
        messages.info(request, 'Lesson deleted succesfully!')
        return redirect('lessons')
    

    return render(request, 'lesson_delete.html', context)

def lesson_update(request, pk):

        lesson = Video.objects.get(pk=pk)
        form = Lesson_form(instance=lesson)

        
        if request.method == 'POST':
                form = Lesson_form(request.POST, instance=lesson)
                if form.is_valid():
                    form.save()
                    messages.info(request, 'Lesson updated succesfully!')
                    return redirect('lessons')
                else :
                    messages(request, 'Something went wrong !')
                    return redirect('lessons')
            

        context = {'form':form}
        return render(request, 'lesson_update.html', context)





# login logout function
def login_function(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)    
            login(request, user)
            return redirect('home')
        

    return render(request, 'login.html', {'form':form})

def logoutfunction(request):
    logout(request)
    return redirect('home')



# contact
def contact(request):
    if request.method=='POST':
        name = request.POST.get('fullname')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        description = request.POST.get('description')
        age = request.POST.get('age')
        myquery = Contact(name=name, phonenumber=phonenumber, email=email, description=description, age=age)
        myquery.save()
        messages.info(request, 'We will answer you soon ')
        return redirect('/')

