from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)




