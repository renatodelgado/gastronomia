from datetime import date, datetime

from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import render



def index(request):
    context = {"dados": 'APIs para o sistema de controle de produtos para as aulas de gastronomia'}
    return render(request, 'index.html', context)


class ReceitaIngredienteViewSet(viewsets.ModelViewSet):  # Crud completo é feito dessa forma
    queryset = ReceitaIngrediente.objects.filter(ativo=True)
    serializer_class = ReceitaIngredienteSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)  # A cada save, colocar automaticamente o usuário da pessoa que está mexendo

class TipoCulinariaViewSet(viewsets.ModelViewSet):
    queryset = TipoCulinaria.objects.filter(ativo=True)
    serializer_class = TipoCulinariaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.filter(ativo=True)
    serializer_class = ReceitaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadeMedida.objects.filter(ativo=True)
    serializer_class = UnidadeMedidaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.filter(ativo=True)
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class PrecoViewSet(viewsets.ModelViewSet):
    queryset = Preco.objects.filter(ativo=True)
    serializer_class = PrecoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.filter(ativo=True)
    serializer_class = ProfessorSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.filter(ativo=True)
    serializer_class = DisciplinaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.filter(ativo=True)
    serializer_class = FornecedorSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class NotaFiscalViewSet(viewsets.ModelViewSet):
    queryset = NotaFiscal.objects.filter(ativo=True)
    serializer_class = NotaFiscalSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.filter(ativo=True)
    serializer_class = LaboratorioSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class AulaReceitaViewSet(viewsets.ModelViewSet):
    queryset = AulaReceita.objects.filter(ativo=True)
    serializer_class = AulaReceitaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.filter(ativo=True)
    serializer_class = AulaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class MovimentoViewSet(viewsets.ModelViewSet):
    queryset = Movimento.objects.filter(ativo=True)
    serializer_class = MovimentoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
