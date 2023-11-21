from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Demanda, Mensagem
from .forms import DemandaForm
from django.urls import reverse_lazy

class Login(TemplateView):
        template_name = 'login.html'

class PaginaInicial(TemplateView):
        template_name = 'index.html'

class DemandaCreateView(CreateView):
        model = Demanda
        template_name = 'demanda-criar.html'
        fields = ['tituloDemanda', 'descricaoDemanda', 'prioridade', 'status', 'prazo', 'dataDeEncerramento']

        def get_success_url(self):
                return reverse_lazy('demanda-detail', args=[str(self.object.id)])

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


# views.py
def criar_demanda(request):
    if request.method == 'POST':
        form = DemandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('demanda-listar.html')
    else:
        form = DemandaForm()

    return render(request, 'demanda-criar.html', {'form': form})


