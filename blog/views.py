from django.http import HttpResponse,request
from django.shortcuts import render
from .models import Artigo, Categoria

def home(request):
    categoria_selecionadas = request.GET.get('categoria')

    if categoria_selecionadas:
        noticias = Artigo.objects.filter(categoria__nome__icontains=categoria_selecionadas)
    else:
        noticias = Artigo.objects.all()

    categorias = Categoria.objects.all()
    contexto = {
        'lista_artigos' : noticias,
        'lista_categorias' : categorias,
    }


    return render(request, "blog/index.html", contexto)

def sobre_nos(request):
    return render(request, "blog/sobre.html")

