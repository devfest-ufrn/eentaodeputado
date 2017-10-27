# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView)

from api.models import Deputado, Proposicao
from api.serializers import DeputadoSerializer, ProposicaoSerializer

# Create your views here.

#DEBUGGER
#print >>sys.stderr, self.kwargs

class DeputadoCreate(CreateAPIView):
	queryset = Deputado.objects.all()
	serializer_class = DeputadoSerializer

class DeputadoList(ListCreateAPIView):
	queryset = Deputado.objects.all()
	serializer_class = DeputadoSerializer

class DeputadoById(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		idParlamentar = self.kwargs['idParlamentar']
		print >>sys.stderr, self.kwargs
		return Deputado.objects.filter(idParlamentar=idParlamentar)

class DeputadoDetalhes(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		deputado = self.kwargs['idParlamentar']
		return Deputado.objects.filter(idParlamentar=deputado).values('nomeParlamentar', 'idParlamentar', 'urlFoto', 'uf', 'partido', 'condicao')


class ProposicaoCreate(CreateAPIView):
	queryset = Proposicao.objects.all()
	serializer_class = ProposicaoSerializer

class ProposicaoList(ListAPIView):
	queryset = Proposicao.objects.all()
	serializer_class = ProposicaoSerializer

class ProposicaoById(ListAPIView):
	serializer_class = ProposicaoSerializer

	def get_queryset(self):
		id_proposicao = self.kwargs['idProposicao']
		return Proposicao.objects.filter(id_proposicao=id_proposicao)

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
		return Deputado.objects.order_by('-qtdPresencas')

class RankingPartido(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		partido = self.kwargs['partido']
		return Deputado.objects.filter(partido=partido).order_by('-produtividade')

class RankingPropostas(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		return Deputado.objects.order_by('-qtdPropostas')


def deputadoProposicoes(request, id):
	pass
def deputadoPresencas(request, id):
	pass
def deputadoAusencias(request, id):
	pass