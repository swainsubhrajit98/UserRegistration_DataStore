from App.models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta():
        model=UserRegistration
        fields='__all__'