from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Demanda, Mensagem
from .forms import DemandaForm
from django.urls import reverse_lazy
#imports do login
from django.contrib.auth.views import LoginView
from django.contrib import messages

from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Demanda
from .forms import DemandaForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Login(LoginView):
        template_name = 'login.html'
        redirect_authenticated_user = True
    
        def get_success_url(self):
                return reverse_lazy('index')
        
        def form_invalid(self, form):
                messages.error(self.request, 'Credenciais inválidas. Por favor, tente novamente.')
                return super().form_invalid(form)

"""         def form_invalid(self, form):
                messages.error(self.request, 'Invalid username or password')
                return self.render_to_response(self.get_context_data(form=form))
 """

@method_decorator(login_required(login_url='login'), name='dispatch')
class PaginaInicial(TemplateView):
        template_name = 'index.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class DemandaCreateView(CreateView):
        model = Demanda
        template_name = 'demanda-criar.html'
        fields = ['tituloDemanda', 'descricaoDemanda', 'prioridade', 'status', 'prazo', 'dataDeEncerramento']

        def get_success_url(self):
                return reverse_lazy('demanda-detail', args=[str(self.object.id)])


@method_decorator(login_required(login_url='login'), name='dispatch')
class DemandaListView(ListView):
        model = Demanda
        template_name = 'demanda-list.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class DemandaDetailView(DetailView):
        model = Demanda
        template_name = 'demanda-detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
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



@method_decorator(login_required(login_url='login'), name='dispatch')
class EditarDemandaView(UpdateView):
    model = Demanda
    form_class = DemandaForm
    template_name = 'demanda-editar.html'
    success_url = reverse_lazy('demanda-listar')  # Redirecionar para a lista de demandas após a edição

    def get_object(self, queryset=None):
        # Retorna a instância de Demanda que está sendo editada
        return Demanda.objects.get(pk=self.kwargs['pk'])


