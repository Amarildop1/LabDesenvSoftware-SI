from django.db import models
# Create your models here.


class Demanda(models.Model):
    tituloDemanda = models.CharField(max_length=40, verbose_name='Nome')
    descricaoDemanda = models.CharField(max_length=200, verbose_name='Descrição')
    prioridade = models.CharField(max_length=30, verbose_name='Prioridade')

    def __str__(self) -> str:
        return super().__str__()
