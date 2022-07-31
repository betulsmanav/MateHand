from django.urls import path
from .views import UserDetailAPIView,UserListAPIView,UserCreateAPIView,RegisterView,logout
from rest_framework.authtoken import views


urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', logout),
    path('list/',UserListAPIView.as_view(), name='users_list'),
    path('create/',UserCreateAPIView.as_view(), name='users_list'),
    path('detail/<int:pk>',UserDetailAPIView.as_view(), name='user_detail'),
]
 





















# CBV
# from store.api.views import UserListCreateAPIView,PostListCreateAPIView,RoomListCreateAPIView,HashtagListCreateAPIView


# urlpatterns = [
#     path('users/',UserListCreateAPIView.as_view() ),
#     path('posts/',PostListCreateAPIView.as_view() ),
#     path('rooms/', RoomListCreateAPIView.as_view()),
#     path('hashtags/',HashtagListCreateAPIView.as_view() ),
# ]
# FBV 
# from .views import user_list_create,post_list_create,room_list_create,hashtag_list_create
# urlpatterns = [
#     path('users/', user_list_create),
#     path('posts/', post_list_create),
#     path('rooms/', room_list_create),
#     path('hashtags/', hashtag_list_create),
 
    
# ]
