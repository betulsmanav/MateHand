from django.contrib import admin
from .models import Follower, UserProfile,UserRoomMembership

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Follower)
admin.site.register(UserRoomMembership)

