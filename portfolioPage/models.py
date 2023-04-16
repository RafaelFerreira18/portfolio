from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=65)
    email = models.CharField(max_length=128)
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
