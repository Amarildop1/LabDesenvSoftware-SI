from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('inicio/', PaginaInicial.as_view(), name='index'),
    path('demanda/criar', DemandaCreateView.as_view(), name='demanda-criar'),
    path('demanda/list', DemandaListView.as_view(), name='demanda-listar'),
    path('demanda/detail/<int:pk>', DemandaDetailView.as_view(), name='demanda-detail'),
    path('enviarMensagem', MensagemCreateView.as_view(), name='enviar-mensagem'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('demanda/editar/<int:pk>/', EditarDemandaView.as_view(), name='editar-demanda'),
     path('demanda/excluir/<int:pk>', DemandaDeleteView.as_view(), name='demanda-excluir'),


]

