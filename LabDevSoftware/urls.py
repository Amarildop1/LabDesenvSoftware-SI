from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('demanda/list', DemandaListView.as_view(), name='demanda-list'),
    path('demanda/detail/<int:pk>', DemandaDetailView.as_view(), name='demanda-detail'),

]


