from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile, CustomUser

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = CustomUser
        #fields = ['email','password1','password2']
        fields = ('email','first_name','last_name')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']