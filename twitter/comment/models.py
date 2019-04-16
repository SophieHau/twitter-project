from django.db import models
from tweet.models import Tweet
from user_profile.models import Profile


class Comment(models.Model):
	text = models.CharField(max_length=280)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('published on')
	tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
	
	class Meta:
		ordering = ['-pub_date']