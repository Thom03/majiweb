from django.urls import path, reverse_lazy

from customers.views import createCustomer, listCustomer, add_show_sites

app_name = "customers"

urlpatterns = [
    path("createcustomer/", createCustomer, name="createCustomer"),
    path("listcustomer/", listCustomer, name="listCustomer"),
    path("sitesview/", add_show_sites, name="sites"),
]
