from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View

from customers.forms import CustomerForm, SiteForm
from customers.models import Customer, Site


# Create your views here.
# Listing all the customers
def listCustomer(request):
    data = {"customers": Customer.objects.all()}
    return render(request, "customers/customerlist.html", data)


def createCustomer(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        customer_form.instance.owner = request.user
        if customer_form.is_valid():
            customer_form.save()
            messages.success(request, "The customer was added successfully.")
        else:
            messages.error(request, "Error adding new customer.")

        return redirect("customers:listCustomer")
    customers_form = CustomerForm()

    return render(request=request, template_name="customers/createcustomer.html", context={'customers_form': customers_form})


# def listSites(request):
#     data = {"customers": Customer.objects.all()}
#     return render(request, "customers/sitemanage.html.html", data)

class SitesView(View):
    context = {"sites": Site.objects.all()}

    def get(self, request):
        if request.method == "POST":
            site_form = SiteForm(request.POST)
            if site_form.is_valid():
                site_form.save()
                messages.success(request, "The Site was added successfully.")
            else:
                messages.error(request, "Error adding new customer.")
        site_form = SiteForm()
        self.context['site_form'] = site_form
        return render(request, 'customers/sitemanage.html', self.context)

