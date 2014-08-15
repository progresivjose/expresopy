from .models import Politic
from politicentities.serializers import PoliticEntitySerializer
from politicfiles.serializers import PoliticFileSerializer
from votes.serializers import VoteSerializer
from rest_framework import serializers

class PoliticSerializer(serializers.ModelSerializer):
	politicentity_to_politic = PoliticEntitySerializer(many=True)
	votes_to_politic         = VoteSerializer(many=True)
	politicfile              = PoliticFileSerializer(many=True)
	class Meta:
		model  = Politic
		fields = (
			'id', 
			'firstname', 
			'lastname', 
			'degree', 
			'biography', 
			'ranking', 
			'image', 
			'political_party',
			'politicentity_to_politic',
			'votes_to_politic',
			'politicfile',)