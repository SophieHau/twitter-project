from django.db import models
from django.contrib.auth.models import User
from user_profile.models import Profile


class Tweet(models.Model):
	text = models.CharField(max_length=280)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('published on')
	like = models.IntegerField(default=0)

	
