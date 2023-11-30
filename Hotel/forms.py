from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import contacto , Tipohabitaciones


class CustomuUserCreationForm(UserCreationForm):
    username =forms.CharField(min_length=4, max_length=20)
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields= ['username', 'email', 'password1','password2']
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email        

#class ReservacionForm(forms.ModelForm):
#    class Meta:
#        model = Reservaciones
#        fields = ['fechaentrada', 'fechasalida', 'iva', 'estado', 'idhabitacion', 'dnihuesped', 'idempleados']

class contactoform(forms.ModelForm):
    class Meta:
        model = contacto
        fields= ["nombre","correo","mensaje"]
        #fiels = "__all__" retorna el orden x defecto
'''
class CustomUserForm(UserCreationForm):
    username =forms.CharField(min_length=4, max_length=20)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email
    def save(self, commit=True):

        try:
            user = super().save(commit=commit)
            grupo_usuario, created = Group.objects.get_or_create(name='Usuario')
            user.groups.add(grupo_usuario)
            return user
        except Exception as e:
            print(f"Error guardando usuario: {e}")
            return None




class TipoHabitacionesform(forms.ModelForm):
    class Meta:
        model = Tipohabitaciones
        fields = ['titulo','idtipohabitacion','imagen1','imagen2','imagen3','imagen4','descripcion','detalle','precio']
        

'''
