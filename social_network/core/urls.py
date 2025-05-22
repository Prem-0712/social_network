from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    



    # Frontend Pages URLs
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('messages/', views.message_view, name='messages'),
    path('create-post/', views.create_post, name='create_post'),
    path('notifications/', views.notifications, name='notifications'),
    path('friends/', views.friends, name='friends'),
    path('search/', views.search_results, name='search_results'),

    
]
