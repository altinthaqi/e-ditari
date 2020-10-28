from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'editari/index.html')

def staff_login(request):
    return render(request, 'editari/staff-login.html')

def parent_login(request):
    return render(request, 'editari/parent-login.html')

def student_login(request):
    return render(request, 'editari/student-login.html')