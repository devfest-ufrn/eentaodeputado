# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from api.models import Deputado, Proposicao
from api.serializers import DeputadoSerializer, ProposicaoSerializer

# Create your views here.

@api_view(['GET'])
def ranking_geral(request):
	
	deputados = Deputado.objects.all()
	deputado_serializer = DeputadoSerializer(deputados, many=True)

	return JsonResponse(deputado_serializer.data, safe=False)

@api_view(['GET'])
def deputado_list(request):

	deputados = Deputado.objects.all()
	deputado_serializer = DeputadoSerializer(deputados, many=True)

	return JsonResponse(deputado_serializer.data, safe=False)

@api_view(['GET'])
def deputadoById(request, identification):
	deputado = Deputado.objects.get(idParlamentar=identification)
	deputado_serializer = DeputadoSerializer(deputado)

	return JsonResponse(deputado_serializer.data, safe=False)

def deputadoDetalhes(request, id):
	pass
def deputadoProposicoes(request, id):
	pass
def deputadoPresencas(request, id):
	pass
def deputadoAusencias(request, id):
	pass

@api_view(['GET'])	
def proposicao_list(request):
	proposicoes = Proposicao.objects.all()
	proposicao_serializer = ProposicaoSerializer(proposicoes, many=True)

	return JsonResponse(proposicao_serializer.data, safe=False)

@api_view(['GET'])
def proposicaoById(request, identification):
	proposicao = Proposicao.objects.get(id_proposicao=identification)
	proposicao_serializer = ProposicaoSerializer(proposicao)

	return JsonResponse(deputado_serializer.data, safe=False)	

def ranking_uf(request, uf):
	pass
def ranking_presencas(request):
	pass
def ranking_propostas(request):
	pass	
		