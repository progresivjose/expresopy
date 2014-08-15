from django.db import models
from entities.models import Entity
from politics.models import Politic
# Create your models here.
class PoliticEntity(models.Model):
	role           = models.CharField(max_length=255)
	description    = models.TextField()
	enrol_date     = models.DateTimeField(auto_now_add=True, blank=True)
	departure_date = models.DateTimeField(auto_now_add=True, blank=True)
	current        = models.BooleanField()
	created        = models.DateTimeField(auto_now_add=True, blank=False)
	modified       = models.DateTimeField(auto_now_add=True, blank=True)
	politic        = models.ForeignKey(Politic, related_name='politicentity_to_politic') 
	entity         = models.ForeignKey(Entity, related_name='politicentity_to_entity') 

	def __unicode__(self):
		return self.role