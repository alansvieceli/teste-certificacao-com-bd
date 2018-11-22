from django.contrib import admin
from .models import Pergunta
from .models import Resposta

admin.site.register(Pergunta)
admin.site.register(Resposta)