# core/forms.py
from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'rows': 5})
    )
    captcha = CaptchaField()
