from django.shortcuts import render, redirect
from django.http import HttpResponse
from marketplace.models import Membro, Genero


# Create your views here.
def index(request):
    # return HttpResponse("<h1>Alô Senai Games!</h1>")
    # request - requisição
    # template - html entre outros
    # context - objetos (python, python com banco de dados)

    Membros = Membro.objects.all()
    return render(request,'marketplace/index.html', {"membros": Membros,})
# Create your views here.

def autentica_membro(request):
    
    Membros = Membro.objects.all()
    generos = Genero.objects.all()
    return render(request, 'marketplace/sou_membro.html',{ 
        "membros": Membros,
        "generos": generos
    }        
      )
    

    

def tecnologia(request):
    return render(request, 'marketplace/tecnologia.html')

def monstra_generos(request):
    return render(request, 'marketplace/sou_membro.html',)