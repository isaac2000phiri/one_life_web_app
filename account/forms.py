from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User

 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'email', 
            'password1', 
            'password2', 
        ]

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')
