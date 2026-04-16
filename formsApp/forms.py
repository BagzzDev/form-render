from django import forms

from .models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ["email", "password"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }