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

def staff_login(request):
    return HttpResponse('<h1> Staff Login </h1>')

def parent_login(request):
    return HttpResponse('<h1> Parent Login </h1>')

def student_login(request):
    return HttpResponse('<h1> Student Login </h1>')