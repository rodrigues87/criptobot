from django.db import models

from ativo.models import Ativo


class Capital(models.Model):
    especie = models.DecimalField(max_digits=20, decimal_places=2)

    def adicionar_capital(self, dinheiro_administrado):
        self.especie = self.especie + dinheiro_administrado

    def __str__(self):
        return self.especie
