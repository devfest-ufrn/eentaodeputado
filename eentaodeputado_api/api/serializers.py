from rest_framework import serializers
from api.models import Deputado

class DeputadoSerializer(serializers.Serializer):
	"""docstring for DeputadoSerializer"""
	nome = serializers.CharField(required=False, allow_blank=True, max_length=200)
