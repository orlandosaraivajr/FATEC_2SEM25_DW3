from django.shortcuts import render
from datetime import datetime
from core.models import FeriadoModel

def feriados(request):
    hoje = datetime.today()
    qs = FeriadoModel.objects.filter(dia=hoje.day).filter(mes=hoje.month)
    if len(qs) == 0:
        contexto = {'feriado':False}
        return render(request, 'feriado.html', contexto)    
    # nome_feriado = qs[0].nome
    nome_feriado = qs.first().nome
    contexto = {'feriado':True, 'nome':nome_feriado}
    return render(request, 'feriado.html', contexto)