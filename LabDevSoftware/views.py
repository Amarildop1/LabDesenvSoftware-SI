from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Demanda, Mensagem
from .forms import DemandaForm
from django.urls import reverse_lazy

class Login(TemplateView):
        template_name = 'login.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
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


def criar_demanda(request):
    if request.method == 'POST':
        form = DemandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('demanda-listar.html')
    else:
        form = DemandaForm()

    return render(request, 'demanda-criar.html', {'form': form})


""" TESTANDO LOGIN DO DJANGO """
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html')  # 'pagina-inicial' é o nome da sua URL inicial

    return render(request, 'login.html')
""" FIM DO TESTANDO LOGIN DO DJANGO """


