# News_api
1. Run the following commands to apply migrations for the database:
```console
$ sudo docker-compose build
$ sudo docker-compose run django_news_api sh -c "python manage.py makemigrations"
$ sudo docker-compose run django_news_api sh -c "python manage.py migrate"
```
2. Run the following command to create some data:
```console
$ sudo docker-compose run django_news_api sh -c "python manage.py create_data"
```
Created data is stored in posts/management/commands/create_data.py

3. Now, run the following command to run your Django application in Docker container:
```console
$ sudo docker-compose up
```
4.1. Navigate to http://0.0.0.0:8000/posts/ on your browser to check the list of posts. 
"GET" Method to check the list of posts.
"POST" Method to create the post. Content:
```json
{
    "title": "",
    "link": "",
    "author_name": id
}
```
4.2. Navigate to http://0.0.0.0:8000/posts/userlist/ on your browser to check the list of posts.
"GET" Method to check the list of users.
"POST" Method to create the user. Content:
```json
{
    "username": "",
    "email": "",
    "password": ""
}
```
4.3. Navigate to http://0.0.0.0:8000/posts/comments/ on your browser to check the list of comments.
"GET" Method to check the list of comments.
"POST" Method to compose the comment. Content:
```json
{
    "post": id,
    "name": id,
    "content": ""
}
```
4.4 Navigate to http://0.0.0.0:8000/posts/(pk)/upvote/ on your browser to upvote the post(id = pk).(You must be authenticated)
Method "GET" not allowed.
"POST" Method to upvote the post.






