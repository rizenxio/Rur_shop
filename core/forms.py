from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'isi namamu',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'isi alamat emailmu',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'isi passwordmu',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'isi passwordmu kembali',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'isi namamu',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'isi passwordmu',
        'class':'w-full py-4 px-6 rounded-xl'
    }))