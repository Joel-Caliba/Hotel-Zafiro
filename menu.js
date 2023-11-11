// NAV DE MOVIL
const nav = document.querySelector("#nav");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");

abrir.addEventListener("click", () => {
    nav.classList.add("visible");
})

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
})


// LOGIN 

// PARTE DE LOGIN Y REGISTER PARA LA ANIMACION

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

// AL PRECIONAR CUENTA SE ABRE EL FORMULARIUO LOGIN

// Obtén una referencia al botón "Cuenta" por su ID
var botonCuenta = document.getElementById("botonCuenta");

// Obtén una referencia a la sección "cuenta" por su clase
var seccionCuenta = document.querySelector(".cuenta");

// Agrega un evento de clic al botón
botonCuenta.addEventListener("click", function() {
    // Verifica si la sección "cuenta" está visible
    if (seccionCuenta.style.display === "none" || seccionCuenta.style.display === "") {
        // Si está oculta, muéstrala
        seccionCuenta.style.display = "block";
    } else {
        // Si está visible, ocúltala
        seccionCuenta.style.display = "none";
    }
});










// ventana emergente
const windowBackground= document.getElementById("ventanaEmergente"),
    windowContainer= document.getElementById("ve-contenedor"),
    openButton= document.getElementById("open-button"),
    closeButton= document.getElementById("close-button")

openButton.addEventListener("click", ()=>{
    windowBackground.style.display="flex"
    document.body.style.overflow="hidden"
    }) 
closeButton.addEventListener("click", ()=>{
    windowBackground.style.display="none"
    document.body.style.overflow="auto"
    }) 