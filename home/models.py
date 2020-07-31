from django.db import models
from django.utils import timezone
from django.conf import settings


class BlogCategory(models.Model):
	name = models.CharField(max_length=64)
	slug = models.SlugField(max_length=64)


class BlogPost(models.Model):
	title = models.CharField(max_length=256)
	slug = models.SlugField(max_length=256)
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	category = models.ForeignKey(
		BlogCategory,
		on_delete=models.SET_NULL,
		null=True,
		blank=True
	)


class BlogImage(models.Model):
	image = models.ImageField(upload_to="blog_posts/")
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
