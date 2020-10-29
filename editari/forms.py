from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Newsletter

class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = ['email']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Mandatory')
    last_name = forms.CharField(max_length=30, required=False, help_text='Mandatory')
    email = forms.EmailField(max_length=254, help_text='email')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        User._meta.get_field('email')._unique = True
        fields = ('first_name', 'last_name', 'email', 'birth_date', 'username', 'password1', 'password2', )
