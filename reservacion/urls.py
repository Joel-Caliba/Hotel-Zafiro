from django.urls import path
from .views import reserva, metodo
app_name = 'reservacion'  # Este es el espacio de nombres

urlpatterns = [
    path('reserva/', reserva, name='reserva'),
    path('metodo/', metodo, name='metodo'),
]  
