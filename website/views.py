from django.shortcuts import render, redirect
from .models import Avaliacao

def index(request):
    return render(request, 'website/index.html')

def avalie(request):
    return render(request, 'website/avalie.html')


def avalie_view(request):
    if request.method == 'POST':
        escolha = request.POST.get('opcao')
        comentario = request.POST.get('comentarios')

        Avaliacao.objects.create(
            opcao=escolha,
            comentario=comentario
        )
        return redirect('index')

    return render(request, 'website/avalie.html')
