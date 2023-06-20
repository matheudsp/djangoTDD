from django.test import TestCase
from django.urls import reverse
from .models import Tarefa


class TarefaTestCase(TestCase):
    def setUp(self):
        self.tarefa1 = Tarefa.objects.create(titulo='Tarefa 1', texto='Texto da tarefa 1')
        self.tarefa2 = Tarefa.objects.create(titulo='Tarefa 2', texto='Texto da tarefa 2')
        
    def test_criar_tarefa(self):
        # Fazer uma requisição POST para criar uma nova tarefa
        response = self.client.post(reverse('criar_tarefa'), {'titulo': 'Nova Tarefa', 'texto': 'Texto da nova tarefa'})
        # Verificar se a tarefa foi criada no banco de dados
        self.assertTrue(Tarefa.objects.filter(titulo='Nova Tarefa', texto='Texto da nova tarefa').exists())
        # Verificar se a tarefa criada está sendo exibida na página de listagem de tarefas
        response = self.client.get(reverse('criar_tarefa'))
        self.assertContains(response, 'Nova Tarefa')
        
    def test_excluir_tarefa(self):
        # Verificar se a tarefa 1 existe antes da exclusão
        self.assertTrue(Tarefa.objects.filter(id=self.tarefa1.id).exists())
        # Fazer uma requisição POST para excluir a tarefa 1
        response = self.client.post(reverse('excluir_tarefa', args=[self.tarefa1.id]))
        # Verificar se a resposta é um redirecionamento para a página de criação de tarefas
        self.assertRedirects(response, reverse('criar_tarefa'))
        # Verificar se a tarefa 1 foi removida do banco de dados
        self.assertFalse(Tarefa.objects.filter(id=self.tarefa1.id).exists())
        # Verificar se a tarefa 2 ainda existe
        self.assertTrue(Tarefa.objects.filter(id=self.tarefa2.id).exists())








