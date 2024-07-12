from django.urls import path
from . import views

urlpatterns =[
    path('index',views.index, name='index'),
    path('auspiciadores', views.auspiciadores, name='auspiciadores'),
    path('apadrinacion', views.apadrinacion, name='apadrinacion'),
    path('adopcionP',views.adopcionP, name='adopcionP'),
    path('adopcionP2',views.adopcionP2, name='adopcionP2'),
    path('perritoAdulto', views.perritoAdulto, name='perritoAdulto'),
    path('perritoCachorro',views.perritoCachorro, name='perritoCachorro'),
    path('adopcionG', views.adopcionG, name='adopcionG'),
    path('gatitoCachorro', views.gatitoCachorro, name='gatitoCachorro'),
    path('gatoAdulto',views.gatoAdulto, name='gatoAdulto'),
    path('gato1',views.gato1, name='gato1'),
    path('perro1', views.perro1, name='perro1'),
    path('formulario', views.formulario, name='formulario'),



   path('listar', views.listar, name='listar'),
   path('agregar',views.agregar, name='agregar'),
   path('eliminar/<str:pk>', views.eliminar, name='eliminar'),
   
]