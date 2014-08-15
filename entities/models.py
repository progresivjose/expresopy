from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EntityType(models.Model):
	name     = models.CharField(max_length=255)
	created  = models.DateTimeField(auto_now_add=True, blank=False)
	modified = models.DateTimeField(auto_now_add=True, blank=True)
	user     = models.ForeignKey(User, related_name='entitytype_to_user')

	def __unicode__(self):
		return self.name

class Entity(models.Model):
	name       = models.CharField(max_length=255)
	created    = models.DateTimeField(auto_now_add=True, blank=False)
	modified   = models.DateTimeField(auto_now_add=True, blank=True)
	entitytype = models.ForeignKey(EntityType, related_name='entity_to_entitytype', blank=False, null=False)
	user       = models.ForeignKey(User, related_name='entity_to_user')

	def __unicode__(self):
		return self.name