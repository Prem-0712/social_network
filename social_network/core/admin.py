from django.contrib import admin
from .models import UserProfile, Post, FriendRequest, Notification, Message

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(FriendRequest)
admin.site.register(Notification)
admin.site.register(Message)
