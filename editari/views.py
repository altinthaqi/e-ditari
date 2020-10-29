from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'editari/index.html')

def staff_register(request):
    return render(request, 'editari/staff-register.html')

def parent_register(request):
    return render(request, 'editari/parent-register.html')

def student_register(request):
    return render(request, 'editari/student-register.html')