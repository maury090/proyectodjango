from django.db import models


class Ayuda(models.Model):
    id_ayuda = models.AutoField(db_column='idAyuda',primary_key=True)
    ayuda = models.CharField(max_length=15, blank=False, null=False)

    def _str_(self):
        return str(self.ayuda)
    
class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=4)
    nombre_producto = models.CharField(max_length=20)
    marca_producto = models.CharField(max_length=20)
    valor_producto = models.CharField(max_length=6)
    id_ayuda = models.ForeignKey('Ayuda', on_delete=models.CASCADE, db_column='idAyuda')

    def _str_(self):
        return str(self.nombre_producto)+ " - " + str(self.marca_producto)
