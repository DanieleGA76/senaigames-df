from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("<h1>Alô Senai Games!</h1>")
    # request - requisição
    # template - html entre outros
    # context - objetos (python, python com banco de dados)
    return render(request,'marketplace/index.html')
# Create your views here.

def autentica_menbro(request):
    dados = {
        1:{"nome": "Visual Novel"},
        2:{"nome": "Plataforma"},
        3:{"nome": "Acao"}
    }
    return render(request, 'marketplace/sou_membro.html', {"cards":dados})

def tecnologia(request):
    return render(request, 'marketplace/tecnologia.html')

def monstra_generos(request):
    return render(request, 'marketplace/sou_membro.html',)