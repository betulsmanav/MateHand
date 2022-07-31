from django.shortcuts import render
from rest_framework import serializers,generics
from users.models import UserProfile
from .serializers import UserProfileSerializer
from store.api.pagination import LimitPagi, Pagination

# Create your views here.
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    pagination_class=LimitPagi

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer