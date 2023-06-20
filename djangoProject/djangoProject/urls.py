from django.urls import path
from djangoApp.views import criar_tarefa, excluir_tarefa


urlpatterns = [
    path('tarefa/excluir/<int:tarefa_id>/', excluir_tarefa, name='excluir_tarefa'),
    path('tarefas/', criar_tarefa, name='criar_tarefa'),
]







