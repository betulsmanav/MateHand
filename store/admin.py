from django.contrib import admin
from .models import  PostHashtag,Room,Hashtag,Post,PostLike,PostComment

# PostHashtag,
class PostAdmin(admin.ModelAdmin):
    fields=('user',
            'content',
            'image',
            'hashtag',
            'room',)






admin.site.register(Room)
admin.site.register(Post,PostAdmin)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(Hashtag)
admin.site.register(PostHashtag)


