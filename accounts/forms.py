from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class GuestForm(forms.Form):
    email = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput())


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Full Name'}
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        ))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Content'}
        ))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ))


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ))
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}
        ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username Already Taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email Already Taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Password must match.')
        return data