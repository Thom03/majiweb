from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
# Site management
class Site(models.Model):
    site_name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created"]
        db_table = "sites"
        verbose_name = _("Site")
        verbose_name_plural = _("Sites")

    def __str__(self):
        return self.site_name


# Customer model for the system
class Customer(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="customers", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    national_id = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=13, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1)
    email = models.EmailField()

    class Meta:
        ordering = ["created"]
        db_table = "customers"
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.first_name
