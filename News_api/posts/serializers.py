from rest_framework import serializers
from posts.models import Post, Comment, Upvote
from django.contrib.auth.models import User



class PostSerializer(serializers.ModelSerializer):
	comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='content')
	upvote = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = ('id',
		          'title',
		          'link',
		          'creation_date',
		          'upvote',
		          'author_name',
		          'comments')

	def get_upvote(self, post):
		return Upvote.objects.filter(post=post).count()



class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id',
			      'post',
		          'name',
		          'content',
		          'creation_date')


class UserSerializer(serializers.ModelSerializer):
	posts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
	comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='content')

	class Meta:
		model = User
		fields = ('username',
			      'email',
			      'password',
			      'posts',
			      'comments')


class UpvoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Upvote
		fields = ('id', )