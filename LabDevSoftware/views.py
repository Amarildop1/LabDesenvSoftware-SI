from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
#import do login
from django.contrib.auth.views import LoginView
from django.contrib import messages

from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView

from .models import Demanda, Mensagem
from .forms import DemandaForm, EncaminharDemandaForm, TarefaForm

from django.views import View



class Login(LoginView):
        template_name = 'login.html'
        redirect_authenticated_user = True
    
        def get_success_url(self):
                return reverse_lazy('index')
        
        def form_invalid(self, form):
                messages.error(self.request, 'Credenciais inválidas. Por favor, tente novamente.')
                return super().form_invalid(form)

        def form_invalid(self, form):
                messages.error(self.request, 'Usuário e(ou) senha inválidos!')
                return self.render_to_response(self.get_context_data(form=form))


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


class DemandaDeleteView(DeleteView):
    model = Demanda
    template_name = 'demanda-excluir.html'
    success_url = reverse_lazy('demanda-listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_demanda'] = self.object.tituloDemanda
        context['descricao_demanda'] = self.object.descricaoDemanda
        context['status_demanda'] = self.object.status
        return context



def listar_demandas(request):
    demandas = Demanda.objects.all()
    return render(request, 'demanda-list.html', {'demandas': demandas})


@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Avaliador').exists(), login_url='login'), name='dispatch')
class EncaminharDemandaView(View):
    template_name = 'encaminhar-demanda.html'

    def get(self, request, pk):
        demanda = get_object_or_404(Demanda, pk=pk)
        form = EncaminharDemandaForm()
        is_avaliador = request.user.groups.filter(name='Avaliador').exists()
        return render(request, self.template_name, {'demanda': demanda, 'form': form, 'is_avaliador': is_avaliador})

    def post(self, request, pk):
        demanda = get_object_or_404(Demanda, pk=pk)
        form = EncaminharDemandaForm(request.POST)
        is_avaliador = request.user.groups.filter(name='Avaliador').exists()

        if form.is_valid():
            # Lógica para encaminhar a demanda (salvar no banco de dados, etc.)
            destinatario = form.cleaned_data['encaminhar_para']

            # Verifica se o destinatário é um avaliador
            if destinatario.groups.filter(name='Avaliador').exists():
                # Atualiza o campo atribuído_a com o usuário Dev selecionado
                demanda.atribuido_a = destinatario
                demanda.save()
                return redirect('demanda-listar')
            else:
                messages.error(request, 'Somente avaliadores podem ser atribuídos a uma demanda.')
        return render(request, self.template_name, {'demanda': demanda, 'form': form, 'is_avaliador': is_avaliador})


@login_required
def criar_tarefa(request, demanda_id):
    demanda = get_object_or_404(Demanda, pk=demanda_id)

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.demanda = demanda
            tarefa.save()
            return redirect('demanda-detail', pk=demanda_id)
    else:
        form = TarefaForm()

    return render(request, 'tarefa-criar.html', {'form': form, 'demanda': demanda})


@login_required
def detalhe_demanda(request, pk):
    demanda = Demanda.objects.get(pk=pk)
    tarefas = demanda.tarefas.all()  # nome do relacionamento

    return render(request, 'demanda-detail.html', {'demanda': demanda, 'tarefas': tarefas})


