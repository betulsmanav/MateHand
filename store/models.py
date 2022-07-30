from django.db import models
import uuid


class UserProfile(models.Model):
    BATCH_CHOICES=[
        ('user',None),
        ('Dr','Doctor'),
        ('Psk','psikolog'),
        ('Dt','dentist'),
        ('Dyt','diyetisyen'),
    ]

    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    bio=models.CharField(max_length=200)
    email=models.EmailField()
    date_of_birth=models.DateField()
    batch=models.CharField(max_length=5,choices=BATCH_CHOICES,default=None)
    profile_avatar=models.ImageField(upload_to='media/avatar', blank=True)
    background_image=models.ImageField(upload_to='media/background', blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)
    phone_number = models.BigIntegerField()

    def __str__(self):
        return f"{self.name} {self.surname} "

class Room(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"

class UserRoomMembership(models.Model):
    user=models.ForeignKey(UserProfile,related_name='user_of_room', on_delete=models.CASCADE)
    room=models.ForeignKey(Room,related_name='followed_room', on_delete=models.CASCADE)
    joined_room_on=models.DateTimeField(auto_now_add=True)
    left_room_on=models.DateTimeField(auto_now=True)




 
        
class Hashtag(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user=models.ForeignKey(UserProfile,related_name='post', on_delete=models.CASCADE)
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
    user=models.ForeignKey(UserProfile,related_name='user_comments', on_delete=models.CASCADE)
    content=models.CharField(max_length=1000)
    created_date=models.DateTimeField(auto_now_add=True)
    
class PostLike(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user=models.ForeignKey(UserProfile,related_name='post_like_user', on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='follower', on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField() # true-like false-dislike

    def __str__(self):
        return f"{self.user} - {self.status}"
    


class Follower(models.Model):
    follower=models.OneToOneField(UserProfile,related_name='follower', on_delete=models.CASCADE)
    followed=models.OneToOneField(UserProfile,related_name='followed', on_delete=models.CASCADE)
    


    





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