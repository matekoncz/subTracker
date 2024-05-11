from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from home.models import Category

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

class FieldGenerator():
    def CustomCategoryField(user):
        cats = Category.objects.filter(user=user)
        choices = []
        for cat in cats:
            choices.append((cat.name, cat.name))
        return forms.ChoiceField(choices=choices,required=True)

class SubscriptionForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['category'] = FieldGenerator.CustomCategoryField(user)

    service_name = forms.CharField(max_length=128,required=True)
    price = forms.DecimalField(required=True,min_value=0)
