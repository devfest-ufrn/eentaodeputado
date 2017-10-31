# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

SEXO_CHOICES = (('M', 'masculino'), ('F', 'feminino'))

ESTADO_CHOICES = (('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'),
					('BA','BA'), ('CE','CE'), ('DF','DF'),
					('ES','ES'), ('GO','GO'), ('MA','MA'),
					('MT','MT'),('MS','MS'), ('MG','MG'),
					('PA','PA'),('PB','PB'), ('PR','PR'), ('PE','PE'),
					('PI','PI'),('RJ','RJ'), ('RN','RN'),
					('RS','RS'), ('RO','RO'),('RR','RR'), 
					('SC','SC'),('SP','SP'), ('SE','SE'), ('TO','TO'))

TIPO_CHOICES = (('MPV', 'MPV'), ('MSC', 'MSC'), ('REQ', 'REQ'), ('PEC', 'PEC'),
				('PRC', 'PRC'), ('PLP', 'PLP'), ('PL', 'PL'), ('PLN', 'PLN'), 
				('PDC', 'PDC'), ('REP', 'REP'))


class Deputado(models.Model):
	idParlamentar = models.IntegerField(blank=True, default=0)
	nome = models.CharField(max_length=200, blank=True, default='')
	nomeParlamentar = models.CharField(max_length=100, blank=True, default='')
	sexo = models.CharField(max_length=9, choices=SEXO_CHOICES, blank=True, default='')
	uf = models.CharField(max_length=2, choices=ESTADO_CHOICES, blank=True, default='')
	partido = models.CharField(max_length=20, blank=True, default='')
	condicao = models.CharField(max_length=20, blank=True, default='')
	email = models.EmailField(max_length=254, blank=True, default='')
	urlFoto = models.URLField(max_length=200, blank=True, default='')
	fone = models.CharField(max_length=9, blank=True, default='')
	qtdPropostas = models.IntegerField(blank=True, default=0)
	qtdPresencas = models.IntegerField(blank=True, default=0)
	produtividade = models.FloatField(blank=True, default=0.0)
		
	def __str__(self):
		return self.nomeParlamentar
	
	class Meta:
		ordering = ('nome',)
		verbose_name = 'deputado'
		verbose_name_plural = 'deputados'

class Proposicao(models.Model):
	id_proposicao = models.IntegerField(blank=True, default=0)
	nome = models.CharField(max_length=200, blank=True, default='')
	numero = models.IntegerField(blank=True, default=0)
	tipo = models.CharField(max_length=3, choices=TIPO_CHOICES,
							blank=True, default='')
	ano = models.IntegerField(blank=True, default=0)
	ementa = models.TextField(blank=True, default='')
	explicacao = models.TextField(blank=True, default='')
	autor = models.CharField(max_length=254, blank=True, default='')
	indexacao = models.TextField(blank=True, default='')
	
	class Meta:
		ordering = ('nome',)
		verbose_name = 'proposicao'
		verbose_name_plural = 'proposicoes'
		
		


