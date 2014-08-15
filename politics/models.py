from django.db import models
from django.contrib.auth.models import User
from politicalparties.models import PoliticalParty
# Create your models here.

class Politic(models.Model):
	firstname       = models.CharField(max_length=255)
	lastname        = models.CharField(max_length=255)
	degree          = models.CharField(max_length=255)
	biography       = models.TextField()
	image           = models.FileField(blank=True, null=True, upload_to="politics")
	ranking         = models.IntegerField(default=1)
	created         = models.DateTimeField(auto_now_add=True, blank=False)
	modified        = models.DateTimeField(auto_now_add=True, blank=True)
	user            = models.ForeignKey(User, related_name='politic_to_user')
	political_party = models.ForeignKey(PoliticalParty, related_name='politic_to_politicalparty')

	def __unicode__(self):
		return self.firstname + ' ' + self.lastname