from django.urls import path
from .views import *

urlpatterns = [
    path('receitaingrediente/', ReceitaIngredienteViewSet.as_view(), name = 'receitaingrediente'),
    path('tipoculinaria/', TipoCulinariaViewSet.as_view(), name = 'tipoculinaria'),
    path('receita/', ReceitaViewSet.as_view(), name = 'receita'),
    path('unidademedida/', UnidadeMedidaViewSet.as_view(), name = 'unidademedida'),
    path('produto/', ProdutoViewSet.as_view(), name = 'produto'),
    path('preco/', PrecoViewSet.as_view(), name = 'preco'),
    path('professor/', ProfessorViewSet.as_view(), name = 'professor'),
    path('disciplina/', DisciplinaViewSet.as_view(), name = 'disciplina'),
    path('fornecedor/', FornecedorViewSet.as_view(), name = 'fornecedor'),
    path('notafiscal/', NotaFiscalViewSet.as_view(), name = 'notafiscal'),
    path('laboratorio/', LaboratorioViewSet.as_view(), name = 'laboratorio'),
    path('aulareceita/', AulaReceitaViewSet.as_view(), name = 'aulareceita'),
    path('aula/', AulaViewSet.as_view(), name = 'aula'),
    path('movimento/', MovimentoViewSet.as_view(), name = 'movimento'),
    path('', index)
]
