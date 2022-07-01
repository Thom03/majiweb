from django import forms
from metering.models import Meter


# Meter form
class MeterForm(forms.ModelForm):
    class Meta:
        model = Meter
        fields = ('meter_serial', 'meter_number', 'meter_status',)
