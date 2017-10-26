from django.conf.urls import  url
from api import views

uf_list = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG',
		'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
		'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
uf = '(?P<uf>' + '|'.join(uf_list) + ')'

urlpatterns = [
	url(r'^create/deputado/$', views.DeputadoCreate.as_view(), name='create-deputado'),
	url(r'^create/proposicao/$', views.ProposicaoCreate.as_view(), name='create-proposicao'),

	url(r'^ranking/$', views.RankingGeral.as_view(), name='ranking-geral'),
	url(r'^ranking/uf/'+ uf +'/$', views.RankingUF.as_view(), name='ranking-federacao'),
	url(r'^ranking/partido/(?P<partido>\w+)/$', views.RankingPartido.as_view(), name='ranking-partido'),
	url(r'^ranking/presencas/$', views.ranking_presencas, name='ranking-presencas'),
	url(r'^ranking/qdtPropostas/$', views.ranking_propostas, name='ranking-propostas'),

	url(r'^deputados/$', views.DeputadoList.as_view(), name='lista-deputados'),
	url(r'^deputados/(?P<idParlamentar>\d+)/$', views.DeputadoById.as_view(), name='lista-deputado-id'),
	url(r'^deputados/(?P<idParlamentar>\d+)/detalhes/$', views.DeputadoDetalhes.as_view(), name='lista-detalhes'),
	url(r'^deputados/(?P<idParlamentar>\d+)/proposicoes/$', views.deputadoProposicoes, name='lista-proposicoes'),
	url(r'^deputados/(?P<idParlamentar>\d+)/presencas/$', views.deputadoPresencas, name='lista-presencas'),
	url(r'^deputados/(?P<idParlamentar>\d+)/ausencias/$', views.deputadoAusencias, name='lista-ausencias'),

	url(r'^proposicoes/$', views.proposicao_list, name='lista-proposicoes'),
	url(r'^proposicoes/(\d+)/$', views.proposicaoById, name='lista-proposicao-id'),
]


