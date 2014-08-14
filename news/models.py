from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.
class New(models.Model):
	title    = models.CharField(max_length=255)
	summary  = models.TextField(blank=False)
	text     = models.TextField(blank=False)
	image    = models.FileField(blank=True, upload_to="news")
	user     = models.ForeignKey(User, related_name="owner")
	visits   = models.IntegerField(default=0)
	created  = models.DateTimeField(auto_now_add=True, blank=False)
	modified = models.DateTimeField(auto_now_add=True, blank=True)
	category = models.ForeignKey(Category, blank=False, null=False, related_name='new_to_category')
	tags     = TaggableManager()

	def __unicode__(self):
		return self.title