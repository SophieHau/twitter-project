from django.urls import path
from . import views


app_name = 'tweet'

urlpatterns = [
	path('', views.index, name='index'),
	path('tweets/add/<int:profile_id>', views.add_tweet, name='add_tweet'),
	path('tweets/remove/<int:profile_id>/<int:tweet_id>', 
		views.delete_tweet, name='delete_tweet'),
	path('tweets/like/<int:tweet_id>', views.like_tweet, name='like_tweet'),
]