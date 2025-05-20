from django.urls import path
from core import views

urlpatterns = [
    path("", views.navbar, name="nav" ),
    path("home/", views.home, name="home"),
    path("user/", views.user, name='user'),
    path("message/", views.message, name='msg'),
    path('footer/', views.footer, name='footer'),
    path("login/", views.login, name='login'),
    path("dashboard/", views.dashboard, name='dash'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-register/', views.register_admin, name='admin_register'),
]
