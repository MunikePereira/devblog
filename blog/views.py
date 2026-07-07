from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Categoria
from .forms import ContatoForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializeres import ArtigoSerializer, CategoriaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

def artigo_detalhes(request, id):
   
    noticia = get_object_or_404(Artigo, id=id)

    categorias = Categoria.objects.all()
    contexto = {
        'artigos' : noticia,
        'lista_categorias' : categorias,
    }
    return render(request, 'blog/artigo_detalhe.html', contexto)


def fale_conosco(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        formulario = ContatoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    
    else:
        formulario = ContatoForm()
    contexto = {
        'form': formulario, 
        'lista_categorias' : categorias,
    }
    return render(request, 'blog/contato.html', contexto)

# APIS REST

@api_view(['GET'])
def api_listar_artigos(request):
    artigos = Artigo.objects.all()

    serializer = ArtigoSerializer(artigos, many=True)
    return Response(serializer.data)

def api_listar_categoria(request):
    
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_criar_artigo(request):
    serializer = ArtigoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)