from django.urls import path, reverse_lazy

from customers.views import createCustomer, listCustomer, SitesView

app_name = "customers"

urlpatterns = [
    path("createcustomer/", createCustomer, name="createCustomer"),
    path("listcustomer/", listCustomer, name="listCustomer"),
    path("sitesview/", SitesView.as_view(), name="sites"),
]
