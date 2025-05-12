from django.db import models

class Avaliacao(models.Model):
    
    encontrado = models.CharField(max_length=3, choices=[('Sim', 'Sim'), ('Nao', 'Não')])
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
