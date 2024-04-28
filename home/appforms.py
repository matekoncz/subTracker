from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64,widget=forms.PasswordInput)

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=128)
    description = forms.CharField(max_length=256)

class SubscriptionForm(forms.Form):
    service_name = forms.CharField(max_length=128)
    price = forms.NumberInput()
    category = forms.CharField(max_length=128)