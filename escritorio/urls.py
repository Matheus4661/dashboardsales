from django.urls import path, re_path
from escritorio.views import *


app_name = 'escritorio'
urlpatterns = [
    path('', HomeView.as_view()),
    path('arquivos/', RelatorioListView.as_view(), name='lista-arquivos'),
    path('criar_arquivos/', RelatorioCreateView.as_view(), name='criar-arquivos'),
    re_path(r'^arquivos/(?P<pk>\d+)$', RelatorioDetailView.as_view(), name='arquivos-detail')
]
