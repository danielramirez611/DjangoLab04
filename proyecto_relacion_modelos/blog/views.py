from django.shortcuts import render
from .models import Entrada

def entradas_por_autor(request, autor_id):
    entradas_autor = Entrada.objects.filter(autor_id=autor_id)
    return render(request, 'blog/entradas_por_autor.html', {'entradas_autor': entradas_autor})

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})
