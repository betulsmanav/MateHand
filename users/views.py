from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import serializers,generics,permissions
from django.contrib.auth.models import User 
from users.models import UserProfile
from .serializers import UserProfileSerializer,RegisterSerializer
from store.api.pagination import LimitPagi, Pagination

# Create your views here.
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    pagination_class=LimitPagi
    # permission_classes=permissions.IsAdminUser

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class=LimitPagi
    # permission_classes=permissions.AllowAny

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        token=Token.objects.create(user=user)
        data=serializer.data
        data['token']=token.key
        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data={
            'message':'succesfully logout'
        }
        return Response(data)
