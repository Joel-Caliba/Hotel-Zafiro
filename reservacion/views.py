from django.shortcuts import render, redirect
from .forms import ReservacionesForm
from .models import Huespedes
def metodo(request):
    return render(request, 'reservacion/metodo.html')


def reserva(request):
    data = {
        "form": ReservacionesForm()
    }

    if request.method == "POST":
        reserva_form = ReservacionesForm(request.POST)
        if reserva_form.is_valid():
            print("es valido")
            # Procesar y guardar los datos del formulario
            reserva = reserva_form.save(commit=False)
            # Crear un nuevo huésped con los datos del formulario
            huesped = Huespedes(
                dni=reserva_form.creaned_data["dni"],
                nombre=reserva_form.cleaned_data['nombre'],
                apellido=reserva_form.cleaned_data['apellido'],
                direccion=reserva_form.cleaned_data['direccion'],
                telefono=reserva_form.cleaned_data['telefono'],
                email=reserva_form.cleaned_data['email']
            )
            huesped.save()

            # Asociar el huésped con la reserva
            reserva.idhuesped = huesped
            reserva.save()

            data["mensaje"] = "Reserva enviada"
            return redirect('reservacion:metodo')

            #return redirect('metodo')  # Redirigir a una página de confirmación o a donde sea necesario

        else:
            data["form"] = reserva_form

    return render(request, 'reservacion/reserva.html', data)

