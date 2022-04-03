from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
	title = models.CharField(
		max_length=250,
		blank=False,
		default=''
	)

	link = models.URLField()

	creation_date = models.DateTimeField(auto_now_add=True)

	author_name = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='posts'
	)

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(
		Post,
		on_delete=models.CASCADE,
		related_name='comments'
	)

	name = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='comments'
	)

	content = models.TextField()

	creation_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('creation_date', )

	def __str__(self):
		return 'Comment {} by {}'.format(self.content, self.name)



class Upvote(models.Model):
	post = models.ForeignKey(
		Post,
		on_delete=models.CASCADE,
		related_name='upvotes'
	)

	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='upvotes'
	)