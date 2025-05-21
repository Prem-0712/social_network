from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ------------------ Admin Auth ------------------

def register_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
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

        if user is not None and user.is_staff:
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


# ------------------ Frontend Pages ------------------

def home(request):
    return render(request, "core/home.html")

def user_profile(request):
    return render(request, "core/user.html")

def message_view(request):
    return render(request, 'core/message.html')

def navbar(request):
    return render(request, 'core/navbar.html')

def footer(request):
    return render(request, 'core/footer.html')

def edit_profile(request):
    return render(request, 'core/edit_profile.html')

def create_post(request):
    return render(request, 'core/create_profile')

def notifications(request):
    return render(request, 'core/notifications.html')

def friends(request):
    return render(request, 'core/friends.html')

def search_results(request):
    return render(request, 'core/search_results.html')
