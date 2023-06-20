
from django.shortcuts import render, redirect
from .models import Tarefa

def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        texto = request.POST['texto']
        tarefa = Tarefa.objects.create(titulo=titulo, texto=texto)
        tarefa.save()

    tarefas = Tarefa.objects.all()
    return render(request, 'tarefa.html', {'tarefas': tarefas})

def excluir_tarefa(request, tarefa_id):
    # Buscar a tarefa pelo ID
    tarefa = Tarefa.objects.get(id=tarefa_id)

    if request.method == 'POST':
        # Excluir a tarefa
        tarefa.delete()
        return redirect('criar_tarefa')

    # Obter todas as tarefas (exceto a excluída)
    tarefas = Tarefa.objects.exclude(id=tarefa_id)

    # Renderizar o template de listagem de tarefas com as tarefas restantes
    return render(request, 'tarefa.html', {'tarefas': tarefas})



