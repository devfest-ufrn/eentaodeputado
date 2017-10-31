from rest_framework import serializers
from api.models import Deputado, Proposicao

class DeputadoSerializer(serializers.ModelSerializer):
	"""docstring for DeputadoSerializer"""
	class Meta:
		model = Deputado
		fields = '__all__'
	
class ProposicaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proposicao
		fields = '__all__'