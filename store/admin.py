from django.contrib import admin
from .models import Follower, UserProfile,Room,Hashtag,Post,PostLike,PostComment, UserRoomMembership

# PostHashtag,
class PostAdmin(admin.ModelAdmin):
    fields=('user',
            'content',
            'image',
            'hashtag',
            'room',)






admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(UserRoomMembership)
admin.site.register(Post,PostAdmin)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(Hashtag)
# admin.site.register(PostHashtag)
admin.site.register(Follower)


