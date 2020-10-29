from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewsletterForm
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

def staff_register(request):
    return render(request, 'editari/staff-register.html')

def parent_register(request):
    return render(request, 'editari/parent-register.html')

def student_register(request):
    return render(request, 'editari/student-register.html')