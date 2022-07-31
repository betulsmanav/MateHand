from django.db import models
import uuid
from django.contrib.auth.models import User



class Room(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"



class Hashtag(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,related_name='post', on_delete=models.CASCADE)
    content=models.TextField(max_length=1000)
    image = models.ImageField(upload_to='media/image', blank=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)
    room=models.ForeignKey(Room,related_name='room', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.room}---{self.user}---{self.content}"

class PostHashtag(models.Model):
    hashtag=models.ForeignKey(Hashtag,related_name='posthashtag', on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='posthashtag', on_delete=models.CASCADE)
 
class PostComment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    post=models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_comments', on_delete=models.CASCADE)
    content=models.CharField(max_length=1000)
    created_date=models.DateTimeField(auto_now_add=True)
    
class PostLike(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,related_name='post_like_user', on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='follower', on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField() # true-like false-dislike

    def __str__(self):
        return f"{self.user} - {self.status}"
    

    


    





# class Media(models.Model):
#     id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
#     alt=models.CharField(max_length=15)
#     name=models.CharField(max_length=50)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updateded_at=models.DateTimeField(auto_now=True)
#     entity_type=models.UUIDField()

    
    # post_media=models.ImageField(upload_to='media/image', blank=True)
    # profile_avatar=models.ImageField(upload_to='media/avatar', blank=True)
    # background_image=models.ImageField()