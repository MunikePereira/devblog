from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, "blog/index.html")

def sobre_nos(request):
    mensagem = "<h1> Sobre o DevBlog </h1> <p> Somos um canal online para você ficar por dentro das noticias do mundo tecnologico </p>"
    return HttpResponse(mensagem)

