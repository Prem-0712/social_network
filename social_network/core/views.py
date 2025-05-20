from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True  # Mark as admin/staff
            user.save()
            messages.success(request, 'Admin account created successfully!')
            return redirect('admin_login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # only allow staff users
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials or not an admin user.")
            return redirect("admin_login")

    return render(request, "core/login.html")

@login_required(login_url="admin_login")
def dashboard(request):
    return render(request, "core/dashboard.html")

def admin_logout(request):
    logout(request)
    return redirect("admin_login")

def navbar(request):
    return render(request, 'core/navbar.html')

def home(request):
    return render(request, "core/home.html")

def user(request):
    return render(request, "core/user.html")

def message(request):
    return render(request, 'core/message.html')

def footer(request):
    return render(request, 'core/footer.html')

def login(request):
    return render (request, "core/login.html")

def dashboard(request):
    return render(request, "core/dashboard.html")