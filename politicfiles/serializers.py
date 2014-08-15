from .models import PoliticFile
from rest_framework import serializers

class PoliticFileSerializer(serializers.ModelSerializer):
	class Meta:
		model  = PoliticFile
		fields = (
			'file',
			'mime_type',
			'pub_date',
			)