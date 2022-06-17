from django.contrib import admin

# Register your models here.
from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "national_id",
        "first_name",
        "middle_name",
        "last_name",
        "phone_number",
    )

    list_filter = ("created",)
