from rest_framework.viewsets import ModelViewSet
from questoes.models import Pergunta, Resposta
from .serializers import PerguntaSerializer, RespostaSerializer, PerguntaComRespostasSerializer


class PerguntaViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


class PerguntaComRespostasViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaComRespostasSerializer


class RespostaViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
