from .models import Politic
from .serializers import PoliticSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PoliticsListView(APIView):
	def get(self, request, format=None):
		politics       = Politic.objects.all()

		firstname = self.request.QUERY_PARAMS.get('firstname', None)
		id = self.request.QUERY_PARAMS.get('id', None)
		if firstname is not None:
			politics = politics.filter(firstname=firstname)
		if id is not None:
			politics = politics.filter(pk=id)

		serializer = PoliticSerializer(politics)
		return Response(serializer.data)
