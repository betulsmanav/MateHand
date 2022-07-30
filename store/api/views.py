# from django.http.response import HttpResponse
# from django.shortcuts import render
# import rest_framework
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView 
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin
# from rest_framework import status

from rest_framework import serializers,generics
from store.api.pagination import LimitPagi, Pagination
from store.models import Hashtag, PostComment, UserProfile,Post,Room
from .serializers import HashtagSerializer, PostCommentSerialiser, UserProfileSerializer,PostSerializer,RoomSerializer


#----------list-create---------
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    pagination_class=LimitPagi
    
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    pagination_class=LimitPagi


class RoomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializer
    pagination_class=LimitPagi
    
class HashtagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hashtag.objects.all().order_by('-id')
    serializer_class = HashtagSerializer
    pagination_class=LimitPagi
    
class CommentsListCreateAPIView(generics.ListCreateAPIView):
    queryset = PostComment.objects.all().order_by('-id')
    serializer_class = PostCommentSerialiser
    pagination_class=LimitPagi

#----------detail-update-delete---------
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
        
class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerialiser
        
class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
        
class HashtagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
        




























# *ApiView
# class UserListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):

#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class PostListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# *ClassBase
# class UserListCreateAPIView(APIView):
#     def get(self,request):
#         querset =  UserProfile.objects.all()    
#         serializer = UserProfileSerializer(querset, many=True)
#         return Response(serializer.data)
    
        
#     def post(self,request):
#         serializer = UserProfileSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class PostListCreateAPIView(APIView):
#     def get(self,request):
#         querset =  Post.objects.all()    
#         serializer = PostSerializer(querset, many=True)
#         return Response(serializer.data)
    
        
#     def post(self,request):
#         serializer = PostSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class RoomListCreateAPIView(APIView):
#     def get(self,request):
#         querset =  Room.objects.all()    
#         serializer = RoomSerializer(querset, many=True)
#         return Response(serializer.data)
    
        
#     def post(self,request):
#         serializer = RoomSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class HashtagListCreateAPIView(APIView):
#     def get(self,request):
#         querset =  Hashtag.objects.all()    
#         serializer = HashtagSerializer(querset, many=True)
#         return Response(serializer.data)
    
        
#     def post(self,request):
#         serializer = HashtagSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# *FunctionBase
# @api_view(['GET', 'POST'])
# def user_list_create(request):
#     if request.method == "GET":
#         querset =  UserProfile.objects.all()    
#         serializer = UserProfileSerializer(querset, many=True)
    
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = UserProfileSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def post_list_create(request):
#     if request.method == "GET":
#         querset =  Post.objects.all()    
#         serializer = PostSerializer(querset, many=True)
    
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])       
# def room_list_create(request):
#     if request.method == "GET":
#         querset =  Room.objects.all()    
#         serializer = RoomSerializer(querset, many=True)
    
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = RoomSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])       
# def hashtag_list_create(request):
#     if request.method == "GET":
#         querset =  Hashtag.objects.all()    
#         serializer = HashtagSerializer(querset, many=True)
    
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = HashtagSerializer(data = request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        