from django.urls import path, reverse_lazy
from metering.views import add_show_meter

app_name = "metering"

urlpatterns = [
    path("meterview/", add_show_meter, name="addshowmeter"),
]