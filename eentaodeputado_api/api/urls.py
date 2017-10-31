from django.conf.urls import  url
from api import views

uf_list = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG',
		'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
		'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
uf = '(?P<uf>' + '|'.join(uf_list) + ')'

urlpatterns = [
	url(r'^ranking/$', views.RankingGeral.as_view(), name='ranking-geral'),
	url(r'^ranking/uf/'+ uf +'/$', views.RankingUF.as_view(), name='ranking-federacao'),
	url(r'^ranking/partido/(?P<partido>\w+)/$', views.RankingPartido.as_view(), name='ranking-partido'),
	url(r'^ranking/presencas/$', views.RankingPresencas.as_view(), name='ranking-presencas'),
	url(r'^ranking/qdtPropostas/$', views.RankingPropostas.as_view(), name='ranking-propostas'),

	url(r'^deputados/$', views.DeputadoList.as_view({'get': 'list', 'post': 'create'}), name='lista-deputados'),
	url(r'^deputados/(?P<idParlamentar>\d+)/$', views.DeputadoList.as_view({'get': 'retrieve'}), name='lista-deputado-id'),
	url(r'^deputados/(?P<idParlamentar>\d+)/detalhes/$', views.DeputadoDetalhes.as_view(), name='lista-detalhes'),
	url(r'^deputados/(?P<idParlamentar>\d+)/proposicoes/$', views.deputadoProposicoes, name='lista-proposicoes'),
	url(r'^deputados/(?P<idParlamentar>\d+)/presencas/$', views.deputadoPresencas, name='lista-presencas'),
	url(r'^deputados/(?P<idParlamentar>\d+)/ausencias/$', views.deputadoAusencias, name='lista-ausencias'),

	url(r'^proposicoes/$', views.ProposicaoList.as_view({'get': 'list', 'post': 'create'}), name='lista-proposicoes'),
	url(r'^proposicoes/(?P<id_proposicao>\d+)/$', views.ProposicaoList.as_view({'get': 'retrieve'}), name='lista-proposicao-id'),
]


