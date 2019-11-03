from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import MyUser
from django.contrib.auth import get_user_model


class UserLoginForm(forms.Form):
    """Form to log in the user"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)
    
    class Meta(MyUser):
        model = MyUser
        fields = ['email','username','password1', 'password2']
    
    def clean_email(self):
        User = get_user_model()
        email = self.cleaned_data.get('email')
        #using the Django ORM to check for existing emails of the same name that was entered
        if User.objects.filter(email=email):
            raise forms.ValidationError('This email is currently being used')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise forms.ValidationError('please confirm your password')
        if password1 != password2:
            raise forms.ValidationError('passwords do not match, please try again')
        return password2