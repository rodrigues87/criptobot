from django.db import models

# Create your models here.
from ativo.models import Ativo
from capital.models import Capital


class Ordem(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    valor_compra = models.DecimalField(max_digits=20, decimal_places=2)
    data_compra = models.CharField(max_length=40)
    valor_venda = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0)
    data_venda = models.CharField(max_length=40, null=True, blank=True)
    lucro = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    esta_ativa = models.BooleanField()

    def verificar_lucro_atual(self):
        self.lucro = self.ativo.valor_de_mercado - self.valor_compra

    def abrir_ordem_compra(self):
        self.valor_compra = self.ativo.valor_de_mercado
        self.esta_ativa = True

        # TODO AQUI PRECISO SEPARAR POR USUARIO

    def fechar_ordem_compra(self):
        self.valor_venda = self.ativo.valor_de_mercado
        self.lucro = self.valor_venda - self.valor_compra
        self.esta_ativa = False

    def __str__(self):
        return self.ativo.nome + " (" + self.ativo.sigla + ")"
