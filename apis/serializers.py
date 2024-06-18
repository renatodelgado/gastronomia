from rest_framework import serializers
from .models import *


class ReceitaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceitaIngrediente
        fields = '__all__'  # Todos podem ser alterados
        read_only_fields = ['ativo']  # Não teria sentido criar um objeto "inativo", apenas modificá-lo


class TipoCulinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCulinaria
        fields = '__all__'
        read_only_fields = ['ativo']


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
        read_only_fields = ['ativo']


class UnidadeMedidaSerializer(serializers.ModelSerializer):
    unidade = serializers.SerializerMethodField()

    def get_unidade(self, obj):
        return f"{obj.sigla} - {obj.descricao}"

    class Meta:
        model = UnidadeMedida
        fields = '__all__'
        read_only_fields = ['ativo']


class ProdutoSerializer(serializers.ModelSerializer):
    unidade = UnidadeMedidaSerializer()
    class Meta:
        model = Produto
        fields = '__all__'
        read_only_fields = ['ativo']


class PrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preco
        fields = '__all__'
        read_only_fields = ['ativo']


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        read_only_fields = ['ativo']

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'
        read_only_fields = ['ativo']


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        read_only_fields = ['ativo']


class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = '__all__'
        read_only_fields = ['ativo']


class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'
        read_only_fields = ['ativo']


class AulaReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaReceita
        fields = '__all__'
        read_only_fields = ['ativo']


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'
        read_only_fields = ['ativo']


class MovimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimento
        fields = '__all__'
        read_only_fields = ['ativo']


class ItemNotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemNotaFiscal
        fields = '__all__'
        read_only_fields = ['ativo']


class ReceitaItemSerializer(serializers.Serializer):
    receita = serializers.CharField(max_length=100)
    tipoculinaria = serializers.CharField(max_length=100)
    qtd_receita = serializers.IntegerField()


class ProdutoItemSerializer(serializers.Serializer):
    ingrediente = serializers.CharField(max_length=100)
    unidade = serializers.CharField(max_length=100)
    qtd_ingrediente = serializers.DecimalField(decimal_places=5, max_digits=11)
    custo = serializers.DecimalField(decimal_places=2, max_digits=11)


class DetalheAulaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    data = serializers.DateField()
    turno = serializers.CharField(max_length=10)
    qtd_aluno = serializers.IntegerField()
    confirmada = serializers.BooleanField()
    professor = serializers.CharField(max_length=200)
    disciplina = serializers.CharField(max_length=200)
    laboratorio = serializers.CharField(max_length=2000)
    receitas = ReceitaItemSerializer(many=True)
    produtos = ProdutoItemSerializer(many=True)


class PosicaoEstoqueSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length = 100)  # Tipo string, com tamanho max de 100
    unidade = serializers.CharField(max_length = 100)
    quantidade = serializers.DecimalField(max_digits = 11, decimal_places = 5)  # Tipo decimal, sendo 11 dígitos, 5 decimais
    preco_medio = serializers.DecimalField(max_digits = 11, decimal_places = 2)
    total = serializers.DecimalField(max_digits = 11, decimal_places = 2)


class NecessidadeCompraSerializer(serializers.Serializer):
    produto = serializers.CharField(max_length = 100)
    unidade = serializers.CharField(max_length = 100)
    quantidade = serializers.DecimalField(max_digits = 11, decimal_places = 5)
    custo_previsto = serializers.DecimalField(max_digits = 11, decimal_places = 2)

class EntradaNotaFiscalSerializer(serializers.Serializer):
    notafiscal = NotaFiscalSerializer()
    produtos = ItemNotaFiscalSerializer(many=True)

class ProdutoItemSerializer(serializers.Serializer):
    ingrediente = serializers.CharField(max_length = 100)
    unidade = serializers.CharField(max_length = 100)
    qtd_ingredientes = serializers.DecimalField(decimal_places = 5, max_digits = 15)
    custo = serializers.DecimalField(decimal_places = 2, max_digits = 11)


class CustoDiarioSerializer(serializers.Serializer):
    data = serializers.DateField()
    valor = serializers.DecimalField(max_digits=11, decimal_places=2)
