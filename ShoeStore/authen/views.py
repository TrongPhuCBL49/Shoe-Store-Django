from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from .models import CustomerUser
from django.utils.http import is_safe_url
# Create your views here.

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        country = form.cleaned_data.get("country")
        phone_number = form.cleaned_data.get("phone_number")
        province = form.cleaned_data.get("province")
        distric = form.cleaned_data.get("distric")
        address = form.cleaned_data.get("address")
        postcode = form.cleaned_data.get("postcode")
        new_user = User.objects.create_superuser(username, email, first_name, last_name, phone_number, country, province, distric, address, postcode, password)
        if new_user is not None:
            return redirect("/authen/login")
    return render(request, 'authen/register.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")
    return render(request, 'authen/login.html', context)
