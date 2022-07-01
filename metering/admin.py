from django.contrib import admin
from metering.models import Meter
# Register your models here.

@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = (
        "meter_serial",
        "meter_number",
        "meter_status"
    )

    list_filter = ("created",)