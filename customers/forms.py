from django import forms
from customers.models import Customer, Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'national_id', 'phone_number', 'email')
