from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def criar_usuario(request):
    # return HttpResponse("<h1>Alô Senai Games!</h1>")
    # request - requisição
    # template - html entre outros
    # context - objetos (python, python com banco de dados)
    return render(request,'crud_base/usuario_lead.html')