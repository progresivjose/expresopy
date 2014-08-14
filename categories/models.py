from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	title    = models.CharField(max_length=255)
	created  = models.DateTimeField(auto_now_add=True, blank=False)
	modified = models.DateTimeField(auto_now_add=True, blank=True)
	user     = models.ForeignKey(User, related_name="category_to_user")
	category = models.ForeignKey('self', null=True, blank=True, related_name='category_to_subcategory')

	def __unicode__(self):
		return self.title