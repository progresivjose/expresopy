from django.db import models

# Create your models here.
class Cartoon(models.Model):
	title    = models.CharField(max_length=255)
	image    = models.FileField(upload_to="cartoons")
	created  = models.DateTimeField(auto_now_add=True, blank=False)
	modified = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.title