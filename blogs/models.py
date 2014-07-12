from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
	title    = models.CharField(max_length=255)
	text     = models.TextField(blank=False)
	image    = models.FileField(blank=True, upload_to="blogs")
	user     = models.ForeignKey(User, related_name="blog_owner")
	visits   = models.IntegerField(default=0)
	created  = models.DateTimeField(auto_now_add=True, blank=False)
	modified = models.DateTimeField(auto_now_add=True, blank=True)
	tags     = TaggableManager()