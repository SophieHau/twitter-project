from django.shortcuts import render, redirect
from django.utils import timezone
from tweet.models import Tweet
from .models import Comment
from django.contrib.auth.decorators import login_required


def add_comment(request, tweet_id):
	tweet = Tweet.objects.get(pk=tweet_id)
	if request.method == 'POST':
		text = request.POST['comment']
		author = tweet.author
		pub_date = timezone.now()
		c = Comment(text=text, author=author, pub_date=pub_date, tweet_id=tweet_id)
		c.save()
		return redirect('tweet:index')

@login_required(login_url='/accounts/login/')
def delete_comment(request, profile_id, comment_id):
		if request.method == 'POST':
			comment = Comment.objects.get(pk=comment_id)
			if comment.author_id == profile_id:
				comment.delete()
				return redirect('tweet:index')
			else:
				return redirect('tweet:index')