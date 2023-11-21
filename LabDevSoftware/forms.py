# forms.py

from django import forms
from .models import Demanda

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['tituloDemanda', 'descricaoDemanda','prioridade', 'status', 'prazo', 'dataDeCriacao', 'dataDeEncerramento']
        exclude = ['dataDeCriacao']

