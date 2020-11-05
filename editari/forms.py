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
    first_name = forms.CharField(max_length=30, required=True, help_text='*')
    last_name = forms.CharField(max_length=30, required=True, help_text='*')
    email = forms.EmailField(max_length=254, required=True, help_text='*')
    birth_date = forms.DateField(help_text='*', widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}))

    class Meta:
        model = User
        User._meta.get_field('email')._unique = True

        help_texts = {
            'username': '*',
            'password1': "Strong password required"

        }
        widgets = {
            'username': forms.TextInput(attrs={'placheholder':'Username'}),
            'pssword': forms.TextInput(attrs={'placheholder': 'Password'})
        }
        fields = ('first_name', 'last_name', 'email', 'birth_date', 'username', 'password1', 'password2',)
