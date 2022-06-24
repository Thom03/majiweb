from django.contrib import admin

# Register your models here.
from customers.models import Customer, Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "site_name",

    )

    list_filter = ("created",)


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
