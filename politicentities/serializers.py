from .models import PoliticEntity
from rest_framework import serializers

class PoliticEntitySerializer(serializers.ModelSerializer):
	class Meta:
		model  = PoliticEntity
		fields = (
			'id', 
			'role', 
			'description', 
			'enrol_date', 
			'departure_date', 
			'current', 
			)