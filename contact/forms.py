from django import forms
from django.core.validators import ValidationError
from .models import Contact
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'eg. john',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@gmail.com',


            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'subject',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'your message',
            })
        }
