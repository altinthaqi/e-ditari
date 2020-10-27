from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1> Editari Home</h1>')

def staff_login(request):
    return HttpResponse('<h1> Staff Login </h1>')

def parent_login(request):
    return HttpResponse('<h1> Parent Login </h1>')

def student_login(request):
    return HttpResponse('<h1> Student Login </h1>')