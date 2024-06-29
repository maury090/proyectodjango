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
    path('orm1',views.orm1,name='orm1'),
    path('crud',views.crud, name='crud'),
    path('crud_agregar', views.crud_agregar, name='crud_agregar'),
    path('crud_del/<str:pk>', views.crud_del, name='crud_del'),
    path('crud_edit/<str:pk>',views.crud_edit, name='crud_edit'),
]