# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView)

from api.models import Deputado, Proposicao
from api.serializers import DeputadoSerializer, ProposicaoSerializer

# Create your views here.

#DEBUGGER
#print >>sys.stderr, self.kwargs

class DeputadoCreate(CreateAPIView):
	queryset = Deputado.objects.all()
	serializer_class = DeputadoSerializer

class DeputadoList(ListAPIView):
	queryset = Deputado.objects.all()
	serializer_class = DeputadoSerializer

class DeputadoById(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		idParlamentar = self.kwargs['idParlamentar']
		return Deputado.objects.filter(idParlamentar=idParlamentar)

class DeputadoDetalhes(RetrieveAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		return Deputado.objects.values_list('-nomeParlamentar', 'idParlamentar', 'urlFoto', 'uf', 'partido', 'condicao')


class ProposicaoCreate(CreateAPIView):
	queryset = Proposicao.objects.all()
	serializer_class = ProposicaoSerializer

class ProposicaoList(ListAPIView):
	queryset = Proposicao.objects.all()
	serializer_class = ProposicaoSerializer

class RankingGeral(ListAPIView):
	queryset = Deputado.objects.all()
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		return Deputado.objects.order_by('-produtividade')

class RankingUF(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		uf = self.kwargs['uf']
		return Deputado.objects.filter(uf=uf).order_by('-produtividade')

class RankingPresencas(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		return Deputado.objects.order_by('-qtd_presencas')

class RankingPartido(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		partido = self.kwargs['partido']
		return Deputado.objects.filter(partido=partido).order_by('-produtividade')

def deputadoProposicoes(request, id):
	pass
def deputadoPresencas(request, id):
	pass
def deputadoAusencias(request, id):
	pass

@api_view(['GET'])	
def proposicao_list(request):
	pass
	'''
	proposicoes = Proposicao.objects.all()
	proposicao_serializer = ProposicaoSerializer(proposicoes, many=True)

	return JsonResponse(proposicao_serializer.data, safe=False)
	'''

@api_view(['GET'])
def proposicaoById(request, identification):
	pass
	'''proposicao = Proposicao.objects.get(id_proposicao=identification)
	proposicao_serializer = ProposicaoSerializer(proposicao)

	return JsonResponse(deputado_serializer.data, safe=False)	
	'''


def ranking_propostas(request):
	pass	