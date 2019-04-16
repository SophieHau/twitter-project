from django.contrib import admin
from .models import Comment, Tweet

admin.site.register(Tweet)
admin.site.register(Comment)