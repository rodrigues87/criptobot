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
    esta_ativa = models.BooleanField(default=False)

    def verificar_lucro_atual(self):
        self.lucro = self.ativo.valor_de_mercado - self.valor_compra

    def abrir_ordem_compra(self):
        if self.esta_ativa is False:
            self.valor_compra = self.ativo.valor_de_mercado

            capital_brl = Capital.objects.get(ativo="BRL")
            capital_ativo = Capital.objects.get(ativo=self.ativo)

            capital_ativo.valor = capital_ativo.valor + self.valor_compra
            capital_ativo.save()

            capital_brl.valor = capital_brl.valor - self.valor_compra
            capital_brl.save()

    def fechar_ordem_compra(self):
        if self.esta_ativa is True:
            self.valor_venda = self.ativo.valor_de_mercado
            self.lucro = self.valor_venda - self.valor_compra
            self.esta_ativa = False

            capital_brl = Capital.objects.get(ativo="BRL")
            capital_ativo = Capital.objects.get(ativo=self.ativo)

            capital_ativo.valor = capital_ativo.valor - self.valor_venda
            capital_ativo.save()

            capital_brl.valor = capital_brl.valor + self.valor_venda
            capital_brl.save()

    def __str__(self):
        return self.ativo.nome + " (" + self.ativo.sigla + ")"
