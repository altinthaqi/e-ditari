from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from editari.forms import NewsletterForm
from editari.models import Post, User
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from editari.forms import TeacherSignUpForm, StudentSignUpForm, ParentSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.template import RequestContext

def index(request):
    form = NewsletterForm()
    template = "editari/index.html"
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Ju keni bere subscribe per njoftimet e reja! ')
        else:
            messages.warning(request, f'Ky email ekziston. Ju lutem zgjedhni ndonje tjeter.')
        return redirect('/')
    context = {
        'form':form
    }
    return render(request, template, context)


#@login_required
def home(request):
    template = "editari/home.html"
    return render(request, template)


def staff_register(request):
    User.is_teacher = True
    User.is_student = False
    User.is_parent = False
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_teacher = True
            user.teacher.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            return redirect(login_user)
    else:
        form = TeacherSignUpForm()
    return render(request, 'editari/register.html', {'form': form})


def student_register(request):
    User.is_student = True
    User.is_teacher = False
    User.is_parent = False
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_student = True
            print("Its at views")
            user.student.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            return redirect(login_user)
    else:
        form = StudentSignUpForm()
    return render(request, 'editari/register.html', {'form': form})


def parent_register(request):
    User.is_parent = True
    User.is_teacher = False
    User.is_student = False
    if request.method == 'POST':
        form = ParentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_parent = True
            user.parent.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            return redirect(login_user)
    else:
        form = ParentSignUpForm()
    return render(request, 'editari/register.html', {'form': form})



def blogs(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'editari/blogs.html', context)

'''
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_teacher = True
            user.teacher.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(login_user)
    else:
        form = SignUpForm()
    return render(request, 'editari/register.html', {'form': form})
    '''


def check_if_user_is_logedin(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
        return login_user(request)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(blogs)
            else:
                messages.error(request,"Username ose passwordi eshte gabim!")
        else:
            messages.error(request,"Username ose passwordi eshte gabim!")
    form = AuthenticationForm()
    return render(request=request, template_name="editari/login.html", context={"login_form":form})
