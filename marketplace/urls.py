# Urls exclusivas do aplicativo marketing
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('membro/', views.autentica_menbro, name='membro'),
    path('tecnologia/', views.tecnologia, name='tecnologia')
]