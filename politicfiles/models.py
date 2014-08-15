from django.db import models
from politics.models import Politic
# Create your models here.
class PoliticFile(models.Model):
	file     = models.FileField(blank=True, null=True, upload_to="politicfiles")
	mime_type = models.CharField(max_length=255)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	created  = models.DateTimeField(auto_now_add=True, blank=False)
	modified = models.DateTimeField(auto_now_add=True, blank=True)
	politic = models.ForeignKey(Politic, related_name='politicfile')

	def __unicode__(self):
		return self.file