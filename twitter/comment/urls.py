from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
	path('comments/add/<int:tweet_id>', views.add_comment, name='add_comment'),
	path('comments/remove/<int:profile_id>/<int:comment_id>', 
		views.delete_comment, name='delete_comment'),
]
