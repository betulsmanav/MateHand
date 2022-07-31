from django.db import models
import uuid
from django.contrib.auth.models import User
from store.models import Room
# Create your models here.
class UserProfile(models.Model):
    BATCH_CHOICES=[
        ('user',None),
        ('Dr','Doctor'),
        ('Psk','psikolog'),
        ('Dt','dentist'),
        ('Dyt','diyetisyen'),
    ]

    id=models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # name=models.CharField(max_length=200)
    # surname=models.CharField(max_length=200)
    # email=models.EmailField()
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    bio=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    batch=models.CharField(max_length=5,choices=BATCH_CHOICES,default=None)
    profile_avatar=models.ImageField(upload_to='media/avatar', blank=True)
    background_image=models.ImageField(upload_to='media/background', blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)
    phone_number = models.BigIntegerField()

    def __str__(self):
        return f"{self.name} {self.surname} "

class UserRoomMembership(models.Model):
    user=models.ForeignKey(UserProfile,related_name='user_of_room', on_delete=models.CASCADE)
    room=models.ForeignKey(Room,related_name='followed_room', on_delete=models.CASCADE)
    joined_room_on=models.DateTimeField(auto_now_add=True)
    left_room_on=models.DateTimeField(auto_now=True)


class Follower(models.Model):
    follower=models.OneToOneField(UserProfile,related_name='follower', on_delete=models.CASCADE)
    followed=models.OneToOneField(UserProfile,related_name='followed', on_delete=models.CASCADE)