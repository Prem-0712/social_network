from django.urls import path
from . import views

urlpatterns = [
    # Admin Auth URLs
    path('admin/register/', views.register_admin, name='register_admin'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/dashboard/', views.dashboard, name='dashboard'),

    # Frontend Pages URLs
    path('', views.home, name='home'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('messages/', views.message_view, name='messages'),
    path('create-post/', views.create_post, name='create_post'),
    path('notifications/', views.notifications, name='notifications'),
    path('friends/', views.friends, name='friends'),
    path('search/', views.search_results, name='search_results'),

    # Optional: if you want to render navbar/footer as separate views (usually these are included in templates, so rarely needed)
    # path('navbar/', views.navbar, name='navbar'),
    # path('footer/', views.footer, name='footer'),
]
