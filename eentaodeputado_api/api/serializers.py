from rest_framework import serializers
from api.models import Deputado, Proposicao

class DeputadoSerializer(serializers.Serializer):
	"""docstring for DeputadoSerializer"""
	class Meta:
		model = Deputado
		fields = '__all__'
	
class ProposicaoSerializer(serializers.Serializer):
	class Meta:
		model = Proposicao
		fields = '__all__'
		read_only_fields = '__all__'