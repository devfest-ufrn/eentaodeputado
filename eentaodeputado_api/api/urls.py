from django.conf.urls import  url
from api import views

uf_list = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG',
		'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
		'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
uf = '(?:' + '|'.join(uf_list) + ')'

urlpatterns = [
	url(r'^ranking/$', views.ranking_geral, name='ranking-geral'),
	url(r'^ranking/uf/'+ uf +'/$', views.ranking_uf, name='ranking-federacao'),
	url(r'^ranking/presencas/$', views.ranking_presencas, name='ranking-presencas'),
	url(r'^ranking/qdtPropostas/$', views.ranking_propostas, name='ranking-propostas'),

	url(r'^deputados/$', views.deputado_list, name='lista-deputados'),
	url(r'^deputados/(\d+)/$', views.deputadoById, name='lista-deputado-id'),
	url(r'^deputados/(\d+)/detalhes/$', views.deputadoDetalhes, name='lista-detalhes'),
	url(r'^deputados/(\d+)/proposicoes/$', views.deputadoProposicoes, name='lista-proposicoes'),
	url(r'^deputados/(\d+)/presencas/$', views.deputadoPresencas, name='lista-presencas'),
	url(r'^deputados/(\d+)/ausencias/$', views.deputadoAusencias, name='lista-ausencias'),

	url(r'^proposicoes/$', views.proposicao_list, name='lista-proposicoes'),
	url(r'^proposicoes/(\d+)/$', views.proposicaoById, name='lista-proposicao-id'),
]


