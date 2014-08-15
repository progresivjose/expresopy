from django.db import models
from politics.models import Politic
# Create your models here.
class Vote(models.Model):
	vote_type = models.IntegerField()
	politic   = models.ForeignKey(Politic, related_name='votes_to_politic')
	created   = models.DateTimeField(auto_now_add=True, blank=False)
	modified  = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.vote_type