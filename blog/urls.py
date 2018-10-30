from django.conf.urls import url
from django.contrib import admin
from users import views as user_views
from . import views

urlpatterns = [
	url(r'^$', views.home, name='blog-home'),
	url(r'^about/', views.about, name='blog-about'),
	url(r'^register/', user_views.register, name='register'),
]