from django.db import models
from datetime import datetime


class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    codigo = models.TextField()
    date = models.DateTimeField('data de publicação', default=datetime.now, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.texto


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name="respostas")
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

    def __unicode__(self):
        return '%d: %s' % (self.id, self.texto)
