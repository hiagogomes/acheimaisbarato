from django.db import models

class Avaliacao(models.Model):
    
    opcao = models.CharField(max_length=3, choices=[('Sim', 'Sim'), ('Nao', 'Não')])
    comentario = models.TextField()
    data_de_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.opcao} - {self.data_de_envio.strftime('%d/%m/%Y %H:%M')}"
