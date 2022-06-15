from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from .forms import UserEditForm, UserRegistration


def dashboard(request):
    users = User.objects.all()

    total_users = users.count()
    context = {"total_users": total_users}
    return render(request, "dashboard/index.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get("password"))
            new_user.save()
            return render(request, "authapp/register_done.html")
    else:
        form = UserRegistration()

    context = {"form": form}

    return render(request, "authapp/register.html", context=context)


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        "form": user_form,
    }
    return render(request, "authapp/edit.html", context=context)


def userList(request):
    data = {"users": User.objects.all()}

    print("print all data", data)

    return render(request, "accounts/userlist.html", data)
