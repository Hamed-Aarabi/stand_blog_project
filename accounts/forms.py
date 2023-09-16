from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError
from .models import Profile
from django.contrib.auth import login


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if User.objects.filter(username=username).exists():
            confirm_user = authenticate(username=username, password=password)
            if confirm_user is None:
                raise ValidationError('Password is wrong.', code='wrong_password')
        else:
            raise ValidationError('Username not found', code='user_not_found')


class RegisterForm(forms.ModelForm):
    # Build form from forms.Modelform
    password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    re_password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Dori'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John', 'required': False}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dori', 'required': False}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'John@gmail.com', 'required': False})
        }

    def clean(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username already taken. Please try another.', code='username_exist')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password.isalpha() == False and password.isdigit() == False:
            if len(password) < 8:
                raise ValidationError('Password is too short', code='pass_short')
        else:
            raise ValidationError('Password must be contain letters and numbers', code='pass_weak')
        return password


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    re_password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))


    def clean(self):
        user = self.cleaned_data['username']
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['re_password']
        if pass1 != pass2:
            raise ValidationError('Passwords not match.', code='reset_pass')
        if not User.objects.filter(username=user).exists():
            raise ValidationError('Username not found', code='reset_usernotfound')

