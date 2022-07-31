from users.models import UserProfile
from rest_framework import serializers
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