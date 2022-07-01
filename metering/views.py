from django.shortcuts import render
from metering.models import Meter
from metering.forms import MeterForm
from django.contrib import messages
# Create your views here.


# Adding and showing water meters
def add_show_meter(request):
    if request.method == "POST":
        meter_form = MeterForm(request.POST)
        if meter_form.is_valid():
            meter_form.save()
            messages.success(request, "The Site was added successfully.")
    else:
        meter_form = MeterForm()
        messages.error(request, "Error Creating new Site.")
    meters = Meter.objects.all()
    return render(request, 'metering/meteraddshow.html', {'meter_form': meter_form, 'meters': meters})
