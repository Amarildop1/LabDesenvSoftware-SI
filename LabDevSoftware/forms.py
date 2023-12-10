# forms.py

from django import forms
from .models import Demanda

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['tituloDemanda', 'descricaoDemanda','prioridade', 'status', 'prazo', 'dataDeCriacao', 'dataDeEncerramento']
        exclude = ['dataDeCriacao']


# ********************* TESTANDO ****************
from django.contrib.auth.models import User

class EncaminharDemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['encaminhar_para']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['encaminhar_para'].queryset = User.objects.all()




