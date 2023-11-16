from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView


class PaginaInicial(TemplateView):
        template_name = 'index.html'

