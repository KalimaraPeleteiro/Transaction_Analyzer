from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class MoneyOperation(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    banco_origem = models.CharField(max_length=1000)
    agencia_origem = models.CharField(max_length=100)
    conta_origem = models.CharField(max_length=100)
    banco_destino = models.CharField(max_length=1000)
    agencia_destino = models.CharField(max_length=100)
    conta_destino = models.CharField(max_length=100)
    valor = models.FloatField()
    data_transacao = models.DateTimeField()
    data_upload = models.DateTimeField(default = datetime.now)