from django.http import HttpResponse,request
from django.shortcuts import render
from .models import Artigo, Categoria

def home(request, categoria_id=None):
    categoria_id = request.GET.get('categoria')

    if categoria_id:
        noticias = Artigo.objects.filter(categoria_id=categoria_id)
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

