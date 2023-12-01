from django.contrib import admin
from .models import contacto, Habitaciones, Tipohabitaciones, Servicios,crear_eventos #, Huespedes, Habitaciones, Reservaciones, Tipohabitaciones, Hotel, Empleados


# Register your models here.
admin.site.register(contacto)
admin.site.register(crear_eventos)
#admin.site.register(Huespedes)
admin.site.register(Habitaciones)
#admin.site.register(Hotel)
admin.site.register(Tipohabitaciones)
#admin.site.register(Empleados)
admin.site.register(Servicios)