from django.shortcuts import render

def natal(request):
    contexto = {'natal':False}
    return render(request, 'natal.html', contexto)