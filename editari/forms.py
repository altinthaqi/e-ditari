from django import forms
from django.forms import ModelForm

from .models import Newsletter

class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = ['email']