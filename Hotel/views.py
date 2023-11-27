from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .forms import contactoform, CustomuUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from .models import Tipohabitaciones,crear_eventos
from django.shortcuts import render, redirect  
#from .forms import ReservacionForm

#def reserva_view(request):
#    if request.method == 'POST':
#        form = ReservacionForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('página_de_confirmación')  # Puedes redirigir a la página de confirmación después de guardar la reserva
#    else:
#        form = ReservacionForm()
#    return render(request, 'tu_template.html', {'form': form})



def home(request):
    return render(request, 'Hotel/home.html')

def ubicacion(request):
    return render(request, 'Hotel/ubicacion.html')

@login_required
def habitaciones(request):
    habitaciones = Tipohabitaciones.objects.all()
    data={
        'habitaciones' : habitaciones
    }
    return render(request, 'Hotel/habitaciones.html',data)
def exit(request):
    logout(request)
    return redirect("home")

# Agregar la vista de restaurantes si es necesario
# def restaurantes(request):
#     return render(request, 'Hotel/restaurantes.html')
# myapp/views.py

def eventos(request):
    eventos = crear_eventos.objects.all()
    data = {
        'eventos' : eventos
    }
    return render(request, 'Hotel/eventos.html', data)
def contacto(request):
    data ={
        "form":contactoform()
    }
    if request.method == "POST" :
        formulariocontacto=contactoform(data=request.POST)
        if formulariocontacto.is_valid():
            formulariocontacto.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulariocontacto
 

    return render(request, 'Hotel/contacto.html',data)

'''
def login(request):
    data ={
        'form': CustomuUserCreationForm()
    }
    if request.method =='POST':
        formulario = CustomuUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password= formulario.cleaned_data["pasword1"])
            login(request, user)
            messages.success(request, "correcto")
            #a home
            return redirect(to="home")
        
        data['form'] = formulario
    return render(request, 'registration/login.html',data)


'''

'''    
def login(request):
    data = {
        "form": CustomUserForm()
    }
    if request.method == "POST":
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # Autentica y renderiza
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Te registraste exitosamente.")
            return redirect('home')  # Asegúrate de que 'home' sea el nombre correcto de tu vista de inicio
        else:
            data['form'] = formulario
            # Mostrar errores de validación en el formulario
            for field_name, errors in formulario.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field_name}: {error}")

    return render(request, "registration/login.html", data)
'''
'''
def login_view(request):
    data = {"form": CustomUserForm()}

    if request.method == "POST":
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save(commit=False)
            user.save()
            login(request, user)

            # Mensajes de depuración
            print(f"Usuario {user.username} autenticado e inició sesión.")
            
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('home')  # Asegúrate de que 'home' sea el nombre correcto de tu vista de inicio
        else:
            data['form'] = formulario
            for field_name, errors in formulario.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field_name}: {error}")

            # Mensajes de depuración
            print("Formulario no válido. No se inició sesión.")
    return render(request, "registration/login.html", data)
'''



#def habitaciones(request):
#    habitaciones = CrearHabitacion.objects.all()
#    return render(request, 'Hotel/habitaciones.html', {'habitaciones': habitaciones})








#crear tipo habaitaciones
#def crearTipohabitacion(request):
#    if request.method == 'POST':
#        tipohabitacion_form = TipoHabitacionesform(request.POST)
#        if tipohabitacion_form.is_valid():
#            tipohabitacion_form.save()
#            return redirect(to="home")



