from django.db import models

# Create your models here.
# Aqui eu vou programar o modelo
# Classes mapeadas com tabelas
# Persistencia?
# Orientação a Objetos
# Classe ===> Tabela
# localhost: 8080 - site
# localhost:8080/admin 
# github 

# herança
class Membro(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=80, null=False, blank=False)
    senha = models.CharField(max_length=50, null=False, blank=False)


    def __str__(self):
        return f"Nome [nome={self.nome}]"

class Genero(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False )

    def __str__(self):
        return self.nome