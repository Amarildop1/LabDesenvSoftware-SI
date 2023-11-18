from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from .models import Demanda

class PaginaInicial(TemplateView):
        template_name = 'index.html'


class DemandaListView(ListView):
        model = Demanda
        template_name = 'demanda-list.html'

class DemandaDetailView(DetailView):
        model = Demanda
        template_name = 'demanda-detail.html'






