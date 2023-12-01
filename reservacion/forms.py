from django import forms
from .models import Reservaciones, Huespedes

class ReservacionesForm(forms.ModelForm):
    # Agregar campos para el huésped
    dni = forms.IntegerField(label='Dni',),
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=40)
    direccion = forms.CharField(label='Dirección', max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=20)
    email = forms.CharField(label='Email', max_length=250)

    class Meta:
        model = Reservaciones
        fields = ['fechaentrada', 'fechasalida', 'cantidadpersona']
       
    # Personalizar widgets o validaciones específicas para cada campo
    nombre = forms.CharField(label='Nombre', max_length=30, widget=forms.TextInput(attrs={'class': 'input', 'type': 'text', 'required': True}))
    apellido = forms.CharField(label='Apellido', max_length=40, widget=forms.TextInput(attrs={'class': 'input', 'type': 'text', 'required': True}))
    fechaentrada = forms.DateField(
    label='Fecha de Entrada',
    widget=forms.DateInput(attrs={'type': 'date', 'id': 'llegada', 'name': 'fecha-llegada', 'class': 'input'}),
    required=True),
    fechasalida = forms.DateField(label='Fecha de Salida', widget=forms.DateInput(attrs={'type': 'date', 'id':'salida', 'name':'fecha-salida', 'class':'input','required': True})),
    cantidad_persona = forms.ChoiceField(
        label='Cantidad de Personas',
        choices=[('', 'Selecciona una opción'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')],
        required=True,
        widget=forms.Select(attrs={'class': 'opciones', 'required': True})
    )
    def clean(self):
        cleaned_data = super().clean()

        # Validar lógica personalizada si es necesario
        fechaentrada = cleaned_data.get('fechaentrada')
        fechasalida = cleaned_data.get('fechasalida')

        if fechaentrada and fechasalida and fechaentrada >= fechasalida:
            raise forms.ValidationError('La fecha de salida debe ser posterior a la fecha de entrada.')

        return cleaned_data
