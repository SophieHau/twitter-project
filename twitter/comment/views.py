from django.shortcuts import render, redirect
from django.utils import timezone
from tweet.models import Tweet
from .models import Comment


def add_comment(request, tweet_id):
	tweet = Tweet.objects.get(pk=tweet_id)
	if request.method == 'POST':
		text = request.POST['comment']
		author = tweet.author
		pub_date = timezone.now()
		c = Comment(text=text, author=author, pub_date=pub_date, tweet_id=tweet_id)
		c.save()
		return redirect('user_profile:show_profile', profile_id=tweet.author_id)

