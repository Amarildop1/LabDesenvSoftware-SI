from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(Demanda)
admin.site.register(Mensagem)
admin.site.register(Tarefa)



