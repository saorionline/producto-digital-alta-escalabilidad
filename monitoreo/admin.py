from django.contrib import admin
from .models import Marcas, Modelos, Vehiculos, PreciosVehiculos, EstadosVehiculo

admin.site.register(Marcas)
admin.site.register(Modelos)
admin.site.register(Vehiculos)
admin.site.register(PreciosVehiculos)
admin.site.register(EstadosVehiculo)