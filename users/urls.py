from django.urls import path
from .views import UserDetailAPIView,UserListCreateAPIView


urlpatterns = [
    # list-create
    path('users/',UserListCreateAPIView.as_view(), name='users_list'),
    #detail-update-delete 
    path('users/<uuid:pk>',UserDetailAPIView.as_view(), name='user_detail'),
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