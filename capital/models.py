from django.db import models

from ativo.models import Ativo


class Capital(models.Model):
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)

    def transferir_valor(self, capital_transferido):

        capital_transferido.valor = capital_transferido.valor + self.valor
        capital_transferido.save()

        self.valor = self.valor - capital_transferido.valor
        self.save()

    def adicionar_capital(self, dinheiro_administrado):
        self.especie = self.especie + dinheiro_administrado
        self.save()

    def __str__(self):
        return self.ativo.sigla
