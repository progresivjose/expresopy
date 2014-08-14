from .models import New
from .serializers import NewSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NewsListView(APIView):
	def get(self, request, format=None):
		news       = New.objects.all()

		title = self.request.QUERY_PARAMS.get('title', None)
		if title is not None:
			news = news.filter(title=title)

		serializer = NewSerializer(news)
		return Response(serializer.data)


class NewDetailView(APIView):
	def get(self, request, pk, format=None):
		try:
			new = New.objects.get(pk=pk)
		except New.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		#incrementar las visitas
		new.visits += 1
		new.save()

		#devolver los datos
		serializer = NewSerializer(new)
		return Response(serializer.data)


		

