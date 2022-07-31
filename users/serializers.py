from dataclasses import field
from rest_framework import serializers

from django.utils.timezone import now 
from rest_framework.validators import UniqueValidator,ValidationError
from django.contrib.auth.password_validation import validate_password
from users.models import UserProfile
from django.contrib.auth.models import User 


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        #validators=> queryset= tum user lari kontrol et benim emailm unique mi bak
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # password User modelinde yok ekliyoruz.
    # ! write_only : ben response olarak gondereyim ama db de gostermesin (sadece yaz)
    # ! read_only : sadece GET de gelsin POST isleminde bunu kullanma (sadece oku)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password], #defaul validate
        style={"input_type": "password"} # parola gorunmesin diye
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    class Meta:
        model=User
        fields = (
            'username',
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        )
     # rest_framework.serializers.py dan override ettik  
     # password=password2 esitmi kontrol ediyoruz degilse error mesaji esitse kontrol edilen atribute donuyor
    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {"password":"Password field is didn't match"}
            )
        return attrs
    def create(self,validated_data):
        validated_data.pop('password2') # db ye kaydedilmesini istemiyorum cikardim
        password=validated_data.pop('password')
        # password set edilmeden dbye kaydedilemez bunu once cikariyorum user kaydedilmeden once set_password ediyorum sonra user save ediyorum
        user=User.objects.create(**validated_data)
        user.set_password(password) # password kaydedilmeden once arkada isleniyor
        user.save()
        return user 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email"
        )


# class CustomTokenSerializer(TokenSerializer):
#     user = UserSerializer(read_only=True)

#     class Meta(TokenSerializer.Meta):
#         fields = (
#             "key",
#             "user"
#         )


class UserProfileSerializer(serializers.ModelSerializer): 
    # days_since_joined = serializers.SerializerMethodField() 
    # post=serializers.SerializerMethodField('get_post')

    class Meta: 
        model = User 
        fields = '__all__' 
    # def get_days_since_joined(self, obj): 
    #     return (now() - obj.created_date).days
    #     # return (now() - obj.created_date).seconds #dakika olarak gostermek istersen   
    # def get_post(self, obj):
    #     return obj.post.all().values("id","content","room_id")


