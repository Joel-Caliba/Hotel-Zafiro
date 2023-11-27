from django.db import models
from datetime import date


# Create your models here.
class contacto(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField()
    mensaje= models.TextField()

    def __str__(self):
        return self.nombre

class Huespedes(models.Model):
    id_huesped = models.AutoField(db_column='IdHuesped', primary_key=True),
    dni = models.IntegerField(max_length=9, unique=True), # Field name made lowercase.
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'huespedes' 

class Empleados(models.Model):
    idempleados = models.AutoField(db_column='IdEmpleados', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=70)
    #idhotel = models.ForeignKey('Hotel', models.DO_NOTHING, db_column='IdHotel', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'empleados'


class Habitaciones(models.Model):
    idhabitacion = models.AutoField(db_column='IdHabitacion', primary_key=True)  # Field name made lowercase.
    numhabitacion = models.CharField(db_column='NumHabitacion', max_length=10)  # Field name made lowercase.
    idtipohabitacion = models.ForeignKey('Tipohabitaciones', models.DO_NOTHING, db_column='IdTipoHabitacion', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'habitaciones'
    def __str__(self):
        return f'nro: {self.numhabitacion}'





#class Planillaconsumo(models.Model):
#    idplanilla = models.AutoField(db_column='IdPlanilla', primary_key=True)  # Field name made lowercase.
#    idreserva = models.ForeignKey('Reservaciones', models.DO_NOTHING, db_column='IdReserva', blank=True, null=True)  # Field name made lowercase.
#    idservicio = models.IntegerField(db_column='IdServicio', blank=True, null=True)  # Field name made lowercase.

#    class Meta:
#        managed = True
#        db_table = 'planillaconsumo'
class crear_eventos(models.Model):
    idevento = models.AutoField(db_column='IdEvento',primary_key=True)
    titulo = models.CharField('titulo', max_length=200, blank=False, null=False)
    imagen = models.ImageField('imagen', upload_to='eventos/', null=False)
    parrafo = models.TextField()
    descripcion = models.TextField('descripcion',null=True, blank=False)
    detalle = models.TextField('detalle', null=True, blank=True)
    


class Tipohabitaciones(models.Model):
    idtipohabitacion = models.AutoField(db_column='IdTipoHabitacion', primary_key=True)  # Field name made lowercase.
    #idhotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='IdHotel', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField('titulo', max_length=200, blank=False ,null=False)
    categoria = models.CharField(max_length=40)
    imagen1 = models.ImageField('imagen1', upload_to='tipohabitacion/', max_length=255, null=True, blank=True)
    imagen2 = models.ImageField('imagen2', upload_to='tipohabitacion/', max_length=255, null=True, blank=True)
    imagen3 = models.ImageField('imagen3', upload_to='tipohabitacion/', max_length=255, null=True, blank=True)
    imagen4 = models.ImageField('imagen4', upload_to='tipohabitacion/', max_length=255, null=True, blank=True)
    descripcion = models.TextField('descripcion',null=True, blank=False)
    detalle = models.TextField('detalle', null=True, blank=True)
    #temporada = models.CharField(max_length=40)
    precio = models.FloatField()

    class Meta:
        managed = True
        db_table = 'tipohabitaciones'
    def __str__(self):
        return f'categoria: {self.categoria}  precio: {self.precio}'
    
#class Cajas(models.Model):
#    idcaja = models.AutoField(db_column='IdCaja', primary_key=True)  # Field name made lowercase.
#    idempleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='idEmpleado', blank=True, null=True)  # Field name made lowercase.
#    fechahoraapert = models.DateTimeField(db_column='FechaHoraApert')  # Field name made lowercase.
#    fechahoracierre = models.DateTimeField(db_column='FechaHoraCierre')  # Field name made lowercase.
#    gastos = models.DecimalField(max_digits=9, decimal_places=2)
#    reservas = models.CharField(max_length=40)
#    saldocierre = models.BigIntegerField(db_column='SaldoCierre')  # Field name made lowercase.
#    class Meta:
#        managed = True
#        db_table = 'cajas'

#class CrearHabitacion(models.Model):
#    titulo=models.CharField(max_length=100)
#    img = models.ImageField(upload_to="habitaciones/img")
#    descripcion =  models.TextField()
#    caracteristica =  models.TextField()
#    date = models.DateField(default= date.today)
#    def __Str__(self):
#        return self.title

#class Hotel(models.Model):
#    idhotel = models.AutoField(db_column='IdHotel', primary_key=True)  # Field name made lowercase.
#    nombre = models.CharField(max_length=40, blank=True, null=True)
#    direccion = models.CharField(db_column='Direccion', max_length=50)  # Field name made lowercase.
#    class Meta:
#        managed = True
#        db_table = 'hotel'

class Servicios(models.Model):
    idservicio = models.AutoField(db_column='IdServicio', primary_key=True)  # Field name made lowercase.
    nombreservicio = models.CharField(db_column='NombreServicio', max_length=40)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=60)  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio')  # Field name made lowercase.
    iva = models.FloatField(db_column='IVA')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    #idhotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='IdHotel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'servicios'