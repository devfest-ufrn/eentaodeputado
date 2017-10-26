from django.conf.urls import  url
from api import views

uf_list = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG',
		'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
		'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
uf = '(?:' + '|'.join(uf_list) + ')'

urlpatterns = [
	url(r'^ranking/$', views.ranking_geral),
	url(r'^ranking/uf/'+ uf +'/$', views.ranking_uf),
	url(r'^ranking/presencas/$', views.ranking_presencas),
	url(r'^ranking/qdtPropostas/$', views.ranking_propostas),

	url(r'^deputados/$', views.deputado_list),
	url(r'^deputados/(\d+)/$', views.deputadoById),
	url(r'^deputados/(\d+)/detalhes/$', views.deputadoDetalhes),
	url(r'^deputados/(\d+)/proposicoes/$', views.deputadoProposicoes),
	url(r'^deputados/(\d+)/presencas/$', views.deputadoPresencas),
	url(r'^deputados/(\d+)/ausencias/$', views.deputadoAusencias),

	url(r'^proposicoes/$', views.proposicao_list),
	url(r'^proposicoes/(\d+)/$', views.proposicaoById),
]


