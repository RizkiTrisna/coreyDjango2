from django.shortcuts import render
from .models import Post
# Create your views here.
posts = [
	{
		'author': 'rzkid',
		'title': 'Blog 1st Post',
		'content': 'First post content',
		'date_posted': 'October 24, 2018'
	},
	{
		'author': 'teta',
		'title': 'Blog 2nd Post',
		'content': 'Second post content',
		'date_posted': 'October 24, 2018'

	}
]
# We don't use this dummy because wh've created that data at database
def home(request):
	context = {
		'posts': Post.objects.all()

	}
	return render(request, 'blog/home.html', context)

def about(request):
	context = {
		'posts': posts

	}
	return render(request, 'blog/about.html', context)