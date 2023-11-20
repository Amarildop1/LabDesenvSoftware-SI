from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('inicio', PaginaInicial.as_view(), name='index'),
    path('demanda/criar', DemandaCreateView.as_view(), name='demanda-criar'),
    path('demanda/list', DemandaListView.as_view(), name='demanda-list'),
    path('demanda/detail/<int:pk>', DemandaDetailView.as_view(), name='demanda-detail'),

]


