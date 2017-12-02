# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from api.models import Deputado, Proposicao
from api.serializers import DeputadoSerializer, ProposicaoSerializer

# Create your views here.

#DEBUGGER
#print >>sys.stderr, self.kwargs

class DeputadoUF(ListAPIView):
    serializer_class = DeputadoSerializer

    def get_queryset(self): 
        return Deputado.objects.filter(uf=self.kwargs['uf'])

class DeputadoList(viewsets.ModelViewSet):
	queryset = Deputado.objects.all()
	serializer_class = DeputadoSerializer
	lookup_field = 'idParlamentar'

class DeputadoDetalhes(ListAPIView):
	queryset = Deputado.objects.all()
	serializer_class = DeputadoSerializer
	def get_queryset(self):
		return Deputado.objects.filter(idParlamentar=self.kwargs['idParlamentar']).values('nomeParlamentar', 'idParlamentar', 'urlFoto', 'uf', 'partido', 'condicao')

class ProposicaoList(viewsets.ModelViewSet):
	queryset = Proposicao.objects.all()
	serializer_class = ProposicaoSerializer
	lookup_field = 'id_proposicao'

class RankingGeral(ListAPIView):
	queryset = Deputado.objects.all()
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		return Deputado.objects.order_by('-produtividade')

class RankingUF(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self): 
		return Deputado.objects.filter(uf=self.kwargs['uf']).order_by('-produtividade')

class RankingPresencas(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		return Deputado.objects.order_by('-qtdPresencas')

class RankingPartido(ListAPIView):
	serializer_class = DeputadoSerializer

	def get_queryset(self):
		return Deputado.objects.filter(partido=self.kwargs['partido']).order_by('-produtividade')

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