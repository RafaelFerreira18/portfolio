from django.db import models


class Message(models.Model):
    nome = models.CharField(max_length=65, db_column="name")
    email = models.CharField(max_length=65)
    mensagem = models.CharField(max_length=5000, db_column="message")

    def __str__(self):
        return self.nome
