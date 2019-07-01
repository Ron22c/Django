from django import forms
from django.contrib.auth.models import User
from usermodule import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserInformationForm(forms.ModelForm):
    class Meta():
        model =  models.UserInformation
        fields = ('profile_url', 'profile_pic')
