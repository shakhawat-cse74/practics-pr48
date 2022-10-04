from dataclasses import field
from tkinter import Widget
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        #fields = ['name','email','password']
        widgets = {'password': forms.PasswordInput()}
        fields = '__all__'