from django.urls import path
from .views import habitaciones, home, ubicacion, exit, login, contacto, eventos


urlpatterns = [
    path('', home, name='home'),
    path('habitaciones/', habitaciones, name='habitaciones'),
    path('ubicacion/', ubicacion, name='ubicacion'),
    path("logout/", exit, name="exit"),
    path('login/', login, name='login'),
    path('contacto/', contacto, name='contacto'),
    path('eventos/', eventos, name='eventos'),
]  
 