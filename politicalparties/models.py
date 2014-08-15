from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PoliticalParty(models.Model):
	name     = models.CharField(max_length=255)
	created  = models.DateTimeField(auto_now_add=True, blank=False)
	modified = models.DateTimeField(auto_now_add=True, blank=True)
	user = models.ForeignKey(User, related_name='politicalparty_to_user')

	def __unicode__(self):
		return self.name