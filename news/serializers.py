from .models import New
from rest_framework import serializers
class NewSerializer(serializers.ModelSerializer):
	# serializando las noticias
	class Meta:
		model  = New
		fields = (
			'id', 
			'title', 
			'summary', 
			'text', 
			'image', 
			'visits', 
			'created', 
			'category', )