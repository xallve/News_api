from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name=views.PostList.name),
    path('userlist/', views.UserList.as_view(), name=views.UserList.name),
    path('comments/', views.CommentList.as_view(), name=views.CommentList.name),
    path('<int:pk>/upvote/', views.VoteCreate.as_view(), name='upvote_post'),   
]