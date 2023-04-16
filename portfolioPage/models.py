from django.db import models


class Message(models.Model):
    nome = models.CharField(max_length=65)
    email = models.CharField(max_length=128)
    mensagem = models.CharField(max_length=5000)

    def __str__(self):
        return self.nome
