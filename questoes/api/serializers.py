from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from questoes.models import Pergunta, Resposta

#https://www.django-rest-framework.org/api-guide/relations/

class PerguntaSerializer(ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ('id', 'texto', 'codigo', 'date')


class RespostaSerializer(ModelSerializer):
    class Meta:
        model = Resposta
        fields = ('id', 'texto', 'correta')


class PerguntaComRespostasSerializer(ModelSerializer):
    respostas = RespostaSerializer(many=True, read_only=True)

    class Meta:
        model = Pergunta
        fields = ('id', 'texto', 'codigo', 'date', 'respostas')
