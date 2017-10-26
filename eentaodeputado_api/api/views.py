# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics

from api.models import Deputado, Proposicao
from api.serializers import DeputadoSerializer, ProposicaoSerializer

# Create your views here.

def ranking_geral(request):
	
	deputados = Deputado.objects.all()
	deputado_serializer = DeputadoSerializer(deputados, many=True)

	return JsonResponse(deputado_serializer.data, safe=False)
	
def deputado_list(request):

	deputados = Deputado.objects.all()
	deputado_serializer = DeputadoSerializer(deputados, many=True)

	return JsonResponse(deputado_serializer.data, safe=False)

def deputadoById(request, id):
	pass
def deputadoDetalhes(request, id):
	pass
def deputadoProposicoes(request, id):
	pass
def deputadoPresencas(request, id):
	pass
def deputadoAusencias(request, id):
	pass
		
def proposicao_list(request):
	proposicoes = Proposicao.objects.all()
	proposicao_serializer = ProposicaoSerializer(proposicoes, many=True)

	return JsonResponse(proposicao_serializer.data, safe=False)

def proposicaoById(request):
	pass	
def ranking_uf(request, uf):
	pass
def ranking_presencas(request):
	pass
def ranking_propostas(request):
	pass	
		