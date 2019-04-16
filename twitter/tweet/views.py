from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from user_profile.models import Profile
from .models import Tweet


def index(request):
	tweets = Tweet.objects.all()
	return render(request, 'index.html', {
			'tweets': tweets
		})

@login_required(login_url='/accounts/login/')
def add_tweet(request, profile_id):
	profile = Profile.objects.get(pk=profile_id)
	if request.method == 'POST':
		text = request.POST['tweet']
		author = profile
		pub_date = timezone.now()
		t = Tweet(text=text, author=author, pub_date=pub_date)
		t.save()
		return redirect('user_profile:show_profile', profile_id=profile.id)

@login_required(login_url='/accounts/login/')
def delete_tweet(request, profile_id, tweet_id):
	if request.method == 'POST':
		tweet = Tweet.objects.filter(pk=tweet_id).delete()
		return redirect('user_profile:show_profile', profile_id=profile_id)


def like_tweet(request, tweet_id):
	if request.method == 'POST':
		tweet = Tweet.objects.get(pk=tweet_id)
		tweet.like += 1
		tweet.save()
		return redirect('tweet:index')



