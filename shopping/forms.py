from django import forms
from django.contrib.auth.forms import User
from .models import User

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User  
        fields = ['email', 'username','password']