from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Demanda, Mensagem

class Login(TemplateView):
        template_name = 'login.html'

class PaginaInicial(TemplateView):
        template_name = 'index.html'

class DemandaCreateView(CreateView):
        model = Demanda
        template_name = 'demanda-criar.html'
        fields = ['tituloDemanda', 'descricaoDemanda','prioridade']

class DemandaListView(ListView):
        model = Demanda
        template_name = 'demanda-list.html'

class DemandaDetailView(DetailView):
        model = Demanda
        template_name = 'demanda-detail.html'


class MensagemCreateView(CreateView):
        model = Mensagem
        template_name = 'mensagem.html'
        fields = ['tituloMensagem', 'conteudo']



