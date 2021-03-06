from django import forms
from django.contrib.auth.models import User


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

        def clean_password2(self):
            cp = self.cleaned_data
            if cp["password"] != cp["password2"]:
                raise forms.ValidationError("Passwords don't match.")
            return cp["password2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
