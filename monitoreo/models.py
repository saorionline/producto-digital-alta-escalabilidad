from django.db import models

class Marcas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    pais_origen = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'MARCAS'

class Modelos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    marca = models.ForeignKey(Marcas, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=100)
    anio_inicio = models.IntegerField()
    tipo_carroceria = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'MODELOS'

class EstadosVehiculo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    factor_depreciacion = models.DecimalField(max_digits=4, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ESTADOS_VEHICULO'

class Vehiculos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    modelo = models.ForeignKey(Modelos, on_delete=models.DO_NOTHING)
    anio_vehiculo = models.IntegerField()
    kilometraje = models.IntegerField()
    estado = models.ForeignKey(EstadosVehiculo, on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'VEHICULOS'

class PreciosVehiculos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.DO_NOTHING)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_precio = models.CharField(max_length=20)
    fuente = models.CharField(max_length=20)
    fecha_precio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'PRECIOS_VEHICULOS'