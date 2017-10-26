# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

SEXO_CHOICES = (('M', 'masculino'), ('F', 'feminino'))
ESTADO_CHOICES = (('','AC'), ('','AL'), ('','AP'), ('','AM'), ('','BA'), ('','CE'), ('','DF'), ('','ES'), ('','GO'),
					('','MA'), ('','MT'),('','MS'), ('','MG'), ('','PA'), ('','PB'), ('','PR'), ('','PE'), ('','PI'),
					('','RJ'), ('','RN'), ('','RS'), ('','RO'), ('','RR'), ('','SC'), ('','SP'), ('','SE'), ('','TO'))
TIPO_CHOICES = (('', 'MPV'), ('', 'MSC'), ('', 'REQ'), ('', 'PEC'), ('', 'PRC'), ('', 'PLP'), ('', 'PL'), ('', 'PLN'), 
				('', 'PDC'), ('', 'REP'))


class Deputado(models.Model):
	nome = models.CharField(max_length=200, blank=True, default='')
	nomeParlamentar = models.CharField(max_length=100, blank=True, default='')
	sexo = models.CharField(max_length=9, choices=SEXO_CHOICES, blank=True, default='')
	uf = models.CharField(max_length=2, choices=ESTADO_CHOICES, blank=True, default='')
	partido = models.CharField(max_length=20, blank=True, default='')
	email = models.EmailField(max_length=254, blank=True, default='')
	urlFoto = models.URLField(max_length=200, blank=True, default='')
	fone = models.CharField(max_length=9, blank=True, default='')
	condicao = models.CharField(max_length=20, blank=True, default='')
	idParlamentar = models.IntegerField(blank=True, default=0)
	
	
	class Meta:
		ordering = ('nome',)
		verbose_name = 'deputado'
		verbose_name_plural = 'deputados'

class Proposicao(models.Model):
	nome = models.CharField(max_length=200, blank=True, default='')
	numero = models.IntegerField(blank=True, default=0)
	tipo = models.CharField(max_length=3, choices=TIPO_CHOICES,
							blank=True, default='')
	ano = models.IntegerField(blank=True, default='')
	numero = models.IntegerField(blank=True, default=0)
	ementa = models.TextField()
	explicacao = models.TextField()
	autor = models.CharField(max_length=254, blank=True, default='')
	indexacao = models.TextField()
	
	class Meta:
		ordering = ('nome',)
		verbose_name = 'proposicao'
		verbose_name_plural = 'proposicoes'
		
		


