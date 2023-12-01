from django.db import models
from Hotel.models import Habitaciones, Huespedes
from django.contrib.auth.models import User
# Create your models here.



class Reservaciones(models.Model):
    idreserva = models.AutoField(db_column='IdReserva', primary_key=True)  # Field name made lowercase.
    fechaentrada = models.DateField(db_column='FechaEntrada')  # Field name made lowercase.
    fechasalida = models.DateField(db_column='FechaSalida')  # Field name made lowercase.
    iva = models.DecimalField(max_digits=5, decimal_places=2,  default=0.00)
    cantidadpersona = models.PositiveIntegerField()
    estado = models.BooleanField(default=True, verbose_name= "Estado")
    idhabitacion = models.ForeignKey(Habitaciones, models.DO_NOTHING, db_column='IdHabitacion', blank=True, null=True)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    idhuesped = models.ForeignKey(Huespedes, models.DO_NOTHING, db_column='idHuesped', blank=True, null=True)
  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reservaciones'
    def __str__(self):
        return f'reserva de habitacion {self.idhabitacion} por {self.idhuesped}'