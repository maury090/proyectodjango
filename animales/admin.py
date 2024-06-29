from django.contrib import admin

from animales.models import Producto, Ayuda

# Register your models here.

admin.site.register(Ayuda)
admin.site.register(Producto)
