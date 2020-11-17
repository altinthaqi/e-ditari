from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewsletterForm, UserUpdateForm, ProfileUpdateForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in, user_logged_out
from editari.forms import SignUpForm
from django import forms
from django.template import RequestContext
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.dispatch import receiver    


# Create your views here.

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
    return register(request, "staff")


def parent_register(request):
    return register(request, "parent")


def student_register(request):
    return register(request, "student")

def blogs(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'editari/blogs.html', context)

def register(request, u_type):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.type = u_type
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(login_user)
    else:
        form = SignUpForm()
    return render(request, 'editari/register.html', {'form': form})


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
                return redirect(blogs)
            else:
                messages.error(request,"Username ose passwordi eshte gabim!")
        else:
            messages.error(request,"Username ose passwordi eshte gabim!")
    form = AuthenticationForm()
    return render(request=request, template_name="editari/login.html", context={"login_form":form})

@login_required
def edit_profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Llogaria juaj eshte bere UPDATE')
            return redirect('edit-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
        }
    template = 'editari/edit_profile.html'
    return render(request, template, context)

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):
    user.profile.is_online = True
    user.profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):
    user.profile.is_online = False
    user.profile.save()