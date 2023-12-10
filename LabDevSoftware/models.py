from django.db import models
# Create your models here.
from auditlog.registry import auditlog
from django.urls import reverse
from django.contrib.auth.models import User

class Demanda(models.Model):
    tituloDemanda = models.CharField(max_length=255)
    descricaoDemanda = models.TextField()

    PRIORITY_CHOICES = [
        ('baixa', 'Baixa'),
        ('normal', 'Normal'),
        ('urgente', 'Urgente'),
        ('maxima', 'Máxima'),
    ]
    prioridade = models.CharField(max_length=20, choices=PRIORITY_CHOICES)

    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('em_andamento', 'Em Andamento'), ('concluida', 'Concluída')])
    prazo = models.DateField()
    dataDeCriacao = models.DateTimeField(auto_now_add=True)
    dataDeEncerramento = models.DateTimeField(null=True, blank=True)

    # Usuário atribuído à demanda
    atribuido_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandas_atribuidas', default=1)

    # Usuário para quem a demanda foi encaminhada
    encaminhar_para = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandas_encaminhadas', null=True, blank=True)

    class Meta:
        ordering = ['prazo', 'dataDeCriacao']

    def __str__(self) -> str:
        return self.tituloDemanda
    
    def get_absolute_url(self):
        return reverse('demanda-detail', kwargs={'pk': self.pk})
        """ return reverse('demanda-detail', args=[str(self.id)]) """

auditlog.register(Demanda)


class Mensagem(models.Model):
    tituloMensagem = models.CharField(max_length=40, verbose_name='Titulo')
    conteudo = models.CharField(max_length=250, verbose_name='Conteúdo da Mensagem')

    def __str__(self) -> str:
        return self.tituloMensagem

auditlog.register(Mensagem)

