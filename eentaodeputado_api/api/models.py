# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Deputado(models.Model):
	nome = models.CharField(max_length=200, blank=True, default='')
	
	class Meta:
		ordering = ('nome',)
			
		

