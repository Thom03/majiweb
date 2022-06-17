from django import forms
from customers.models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'national_id', 'phone_number', 'email')