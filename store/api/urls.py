from django.urls import path
from store.api.views import CommentDetailAPIView, CommentsListCreateAPIView, HashtagDetailAPIView, PostDetailAPIView,PostListCreateAPIView, RoomDetailAPIView,UserListCreateAPIView,RoomListCreateAPIView,HashtagListCreateAPIView,UserDetailAPIView


urlpatterns = [
    # list-create
    path('users/',UserListCreateAPIView.as_view(), name='users_list'),
    path('posts/',PostListCreateAPIView.as_view(), name='posts_list'),
    path('rooms/', RoomListCreateAPIView.as_view(), name='rooms_list'),
    path('hashtags/',HashtagListCreateAPIView.as_view(), name='hashtags_list'),
    path('comments/',CommentsListCreateAPIView.as_view(), name='comments_list'),
    #detail-update-delete 
    path('users/<uuid:pk>',UserDetailAPIView.as_view(), name='user_detail'),
    path('posts/<uuid:pk>',PostDetailAPIView.as_view(), name='post_detail'),
    path('rooms/<uuid:pk>', RoomDetailAPIView.as_view(), name='room_detail'),
    path('hashtags/<uuid:pk>',HashtagDetailAPIView.as_view(), name='hashtag_detail'),
    path('comments/<uuid:pk>',CommentDetailAPIView.as_view(), name='comment_detail'),
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
