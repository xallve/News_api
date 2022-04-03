from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions
from posts.serializers import PostSerializer, CommentSerializer, UserSerializer, UpvoteSerializer
from django.contrib.auth.models import User
from posts.models import Post, Comment, Upvote
from rest_framework.exceptions import ValidationError



class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	name = 'post-list'

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name = 'comment-list'


class VoteCreate(generics.CreateAPIView):
	serializer_class = UpvoteSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		user = self.request.user
		post = Post.objects.get(pk=self.kwargs['pk'])
		return Upvote.objects.filter(post=post, user=user)

	def perform_create(self, serializer):
		if self.get_queryset().exists():
			raise VaidationError('You have already upvoted this')
		serializer.save(post=Post.objects.get(pk=self.kwargs['pk']), user=self.request.user)