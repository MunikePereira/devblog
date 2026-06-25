from django.http import HttpResponse

def home(request):
    mensagem = "<h1> Bem-vindo ao DevBLog</h1> <p> Em breve, artigos aqui. </p>"

    return HttpResponse(mensagem)

def sobre_nos(request):
    mensagem = "<h1> Sobre o DevBlog </h1> <p> Somos um canal online para você ficar por dentro das noticias do mundo tecnologico </p>"
    return HttpResponse(mensagem)

