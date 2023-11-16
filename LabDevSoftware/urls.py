from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),

]


