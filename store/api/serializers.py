from dataclasses import field
from rest_framework import serializers
from store.models import Hashtag, Post, PostComment, Room,UserProfile
from django.utils.timezone import now 

class UserProfileSerializer(serializers.ModelSerializer): 
    days_since_joined = serializers.SerializerMethodField() 
    post=serializers.SerializerMethodField('get_post')

    class Meta: 
        model = UserProfile  
        fields = '__all__' 
    def get_days_since_joined(self, obj): 
        return (now() - obj.created_date).days
        # return (now() - obj.created_date).seconds #dakika olarak gostermek istersen   
    def get_post(self, obj):
        return obj.post.all().values("id","content","room_id")


class PostCommentSerialiser(serializers.ModelSerializer):
    class Meta:
        model=PostComment
        # exclude=['post_id']
        fields='__all__'



class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hashtag
        fields=('name',)



class PostSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField() 
    comments=serializers.SerializerMethodField('get_comments')
    follower=serializers.SerializerMethodField('get_follower')
    posthashtag=serializers.SerializerMethodField('get_posthashtag')
    class Meta:
        model=Post
        fields =(
            'user',
            'content',
            'image',
            'room',
            'posthashtag',
            'comments',
            'days_since_joined',
            'follower')
        # fields='__all__'
    
    def get_days_since_joined(self, obj): 
        return (now() - obj.publish_date).days
        # return (now() - obj.publish_date).seconds #dakika olarak gostermek istersen  
          
    def get_comments(self, obj):
        return obj.comments.all().values("user","content")
    def get_posthashtag(self, obj):
        return obj.posthashtag.all().values('hashtag')
    def get_follower(self, obj):
        return obj.follower.all().values('user')
    
    

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=[
            "id","title","created_date"
        ]



    