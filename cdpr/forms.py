from dataclasses import field
from tkinter import Label
from cdpr.models import Register
from django.contrib.auth.models import User
from django import forms

class SignUp(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(label="Mobile", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','mobile','email','password']
        # fields = "__all__"

class LoginForm(forms.ModelForm):
    mobile = forms.CharField(label="Mobile",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['mobile','password']