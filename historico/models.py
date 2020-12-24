from django.db import models


# Create your models here.


class Historico(models.Model):
    date = models.CharField(max_length=40)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    previsao = models.BooleanField()
    acertou = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.date
