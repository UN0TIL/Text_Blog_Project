from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Profile


class UpdateUserForm(forms.ModelForm):
    user_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Username'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'E-mail'}))

    class Meta:
        model = User
        fields = ['user_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control mb-1'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Enter First Name'}))
    second_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Enter Last Name'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Enter username'}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Enter E-mail'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Username'}))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control mb-1", 'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']