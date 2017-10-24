# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from api.models import Deputado
from api.serializers import DeputadoSerializer

# Create your views here.

def ranking_geral(request):
	
	deputados = Deputado.objects.all()
	deputado_serializer = DeputadoSerializer(deputados, many=True)

	return JsonResponse(deputado_serializer.data, safe=False)