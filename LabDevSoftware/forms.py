from django import forms
from django.contrib.auth.models import User
from .models import Demanda, Tarefa


class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['tituloDemanda', 'descricaoDemanda','prioridade', 'status', 'prazo', 'dataDeCriacao', 'dataDeEncerramento']
        exclude = ['dataDeCriacao']


class EncaminharDemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['encaminhar_para']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['encaminhar_para'].queryset = User.objects.exclude(username='admin')


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['tituloTarefa']


