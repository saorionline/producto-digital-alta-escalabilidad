from django.contrib import admin
from .models import Marcas, Modelos, Vehiculos, PreciosVehiculos, EstadosVehiculo


@admin.register(Marcas)
class MarcasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais_origen', 'fecha_creacion', 'activo')
    search_fields = ('nombre',)


@admin.register(Modelos)
class ModelosAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'nombre', 'anio_inicio', 'tipo_carroceria')
    list_filter = ('marca', 'tipo_carroceria')


@admin.register(EstadosVehiculo)
class EstadosVehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'factor_depreciacion')


@admin.register(Vehiculos)
class VehiculosAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'anio_vehiculo', 'kilometraje', 'estado', 'color')
    list_filter = ('estado', 'modelo__marca')


@admin.register(PreciosVehiculos)
class PreciosVehiculosAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehiculo', 'precio', 'tipo_precio', 'fuente', 'fecha_precio')
    list_filter = ('tipo_precio', 'fuente')
    date_hierarchy = 'fecha_precio'
