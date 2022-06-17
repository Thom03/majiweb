from django.contrib import messages
from django.shortcuts import render, redirect
from customers.forms import CustomerForm
from customers.models import Customer


# Create your views here.
# Listing all the customers
def listCustomer(request):
    data = {"users": Customer.objects.all()}

    # print("print all data", data)

    return render(request, "customers/customerlist.html", data)


def createCustomer(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            messages.success(request, "The customer was added successfully.")
        else:
            messages.error(request, "Error adding new customer.")

        return redirect("customer:customerlist")
    customers_form = CustomerForm()

    return render(request=request, template_name="customers/createcustomer.html", context={'customers_form': customers_form})
