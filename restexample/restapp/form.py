from django import forms
from .models import Employee

class empForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'email', 'password', 'phone']