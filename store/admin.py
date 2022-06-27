from django.contrib import admin
from .models import Follower,PostHashtag, UserProfile,Room,Hashtag,Post,PostLike,PostComment, UserRoomMembership


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(UserRoomMembership)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(Hashtag)
admin.site.register(PostHashtag)
admin.site.register(Follower)


# @admin.register(Post)
# class CourseAdmin(admin.ModelAdmin):
#     list_display=('user','room','hashtag') #--> istediğimiz sütun eklenebilir fieldlere göre
#     list_filter=('user','room','hashtag') #--> filtreleme
#     search_fields = ('user','room','hashtag','content') #--> admin page de search imkanı sağlar