from django.db import models
from customers.models import Customer
from django.utils.translation import gettext_lazy as _


# Create your models here.
METER_STATUS_CHOICES = (
    ("Active", "ACTIVE"),
    ("Inactive", "INACTIVE"),

)

# Meters Models
class Meter(models.Model):
    customer = models.ForeignKey("customers.Customer", related_name="customers", on_delete=models.CASCADE)
    meter_serial = models.CharField(max_length=30, blank=True)
    meter_number = models.CharField(max_length=30, blank=True)
    meter_status = models.CharField(max_length=30,
                                    choices=METER_STATUS_CHOICES,
                                    default='1')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]
        db_table = "meters"
        verbose_name = _("Meter")
        verbose_name_plural = _("Meters")

    def __str__(self):
        return self.meter_serial
