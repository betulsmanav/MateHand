from dataclasses import field
from rest_framework import serializers
from store.models import Hashtag, Post, PostComment, PostHashtag, Room,UserProfile,PostLike
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




class PostHashtagSerializer(serializers.ModelSerializer):
    hashtag_name = serializers.ReadOnlyField(source='hashtag.name')

    class Meta:
        model = PostHashtag
        fields = ('hashtag_name')


class PostSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField() 
    comments=serializers.SerializerMethodField('get_comments')
    follower=serializers.StringRelatedField(many=True)
    hashtag=PostHashtagSerializer(source='posthashtag_set',many=True)
    class Meta:
        model=Post
        fields = ['user','content','image','room','hashtag','comments','days_since_joined','follower']
        # fields='__all__'
    
    def get_days_since_joined(self, obj): 
        return (now() - obj.publish_date).days
        # return (now() - obj.publish_date).seconds #dakika olarak gostermek istersen  
          
    def get_comments(self, obj):
        return obj.comments.all().values("user","content")
    # def get_hashtag(self, obj):
    #     return obj.hashtag.all().values('hashtag')
    

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=[
            "id","title","created_date"
        ]



    #   https://stackoverflow.com/questions/41976819/django-serialize-a-model-with-a-many-to-many-relationship-with-a-through-argume
    