from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Post

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


@login_required(login_url='login')
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('dashboard')
    return render(request, 'core/admin_dashboard.html')


@login_required(login_url='login')
def user_dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    return render(request, 'core/dashboard.html')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')


# ------------------ Frontend Pages ------------------

def home(request):
    return render(request, "core/home.html")

@login_required
def profile(request):
    user = request.user
    user_posts = Post.objects.filter(user=user).order_by('-created_at')
    context = {
        'user': user,
        'posts': user_posts,
    }
    return render(request, 'core/profile.html', context)

def message_view(request):
    return render(request, 'core/message.html')

def navbar(request):
    return render(request, 'core/navbar.html')

def footer(request):
    return render(request, 'core/footer.html')

def edit_profile(request):
    return render(request, 'core/edit_profile.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        
        Post.objects.create(
            user=request.user,
            content=content,
            image=image,
            video=video
        )
        return redirect('profile')  # Or wherever you want to redirect
    return redirect('profile')

def notifications(request):
    return render(request, 'core/notifications.html')

def friends(request):
    return render(request, 'core/friends.html')

def search_results(request):
    return render(request, 'core/search_results.html')
