from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post

class Command(BaseCommand):
	help = 'Creation of data'

	def handle(self, *args, **options):
		user1, _ = User.objects.get_or_create(
			username='user1',
			email='user1@email.com'
		)
		user1.set_password('password')
		user1.save()

		user2, _ = User.objects.get_or_create(
			username='user2',
			email='user2@email.com'
		)
		user2.set_password('password')
		user2.save()

		user3, _ = User.objects.get_or_create(
			username='user3',
			email='user3@email.com'
		)
		user3.set_password('password')
		user3.save()

		post1, _ = Post.objects.get_or_create(
			title='This is post1',
			link='https://tailscale.com/blog/database-for-2022/',
			author_name=user1
		)

		post2, _ = Post.objects.get_or_create(
			title='This is post2',
			link='https://qoiformat.org/',
			author_name=user2
		)

		post3, _ = Post.objects.get_or_create(
			title='This is post3',
			link='https://vimcolorschemes.com/',
			author_name=user3
		)