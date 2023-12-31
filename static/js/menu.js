// Mostrar background del nav al bajar

window.addEventListener("scroll", function(){
    var header = document.querySelector(".header");
    header.classList.toggle("abajo", window.scrollY>0);
})


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

// Inicio de sesion
const botonCuenta = document.getElementById("button-text");
    botonCuenta.addEventListener("click", ()=>{
        var loginHTML = window.open("LoginRegister/login.html");
    })


// ventana emergente
const windowBackground= document.getElementById("ventanaEmergente"),
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


// ventana emergente para Habitación Doble
const ventanaEmergenteDoble = document.getElementById("ventanaEmergenteDoble"),
    openButtonDoble = document.getElementById("open-button-doble"),
    closeButtonDoble = document.getElementById("close-button-doble");

openButtonDoble.addEventListener("click", () => {
    ventanaEmergenteDoble.style.display = "flex";
    document.body.style.overflow = "hidden";
});

closeButtonDoble.addEventListener("click", () => {
    ventanaEmergenteDoble.style.display = "none";
    document.body.style.overflow = "auto";
});


// ventana emergente para Habitación Familiar
const ventanaEmergenteFamiliar = document.getElementById("ventanaEmergenteFamiliar"),
    openButtonFamiliar = document.getElementById("open-button-familiar"),
    closeButtonFamiliar = document.getElementById("close-button-familiar");

openButtonFamiliar.addEventListener("click", () => {
    ventanaEmergenteFamiliar.style.display = "flex";
    document.body.style.overflow = "hidden";
});

closeButtonFamiliar.addEventListener("click", () => {
    ventanaEmergenteFamiliar.style.display = "none";
    document.body.style.overflow = "auto";
});


// Funcion para que al presionar el boton reserva de abra un html

var btnReservar = document.getElementById('open-reserva');

btnReservar.addEventListener('click', function() {

    window.location.href = 'Reservas/reserva.html';
});


// CAROUSEL 1
let slideIndex = 1;
showSlides(slideIndex)

function plusSlides(n){
    showSlides(slideIndex += n)
}
function currentSlide(n){
    showSlides(slideIndex = n)
}
function showSlides(n){
    let i;
    let slides = document.querySelectorAll(".mySlides");
    let quadrates = document.querySelectorAll(".quadrate"); 
    if(n > slides.length) slideIndex = 1
    if(n < 1) slideIndex = slides.length
    for(i = 0; i < slides.length; i++){
        slides[i].style.display = "none"
    }
    for(i = 0; i < quadrates.length;i++){
        quadrates[i].className = quadrates[i].className.replace("active-carousel","")
    }
    slides[slideIndex-1].style.display = "block";
    quadrates[slideIndex-1].className += " active-carousel";
}

// carousel 2
let slideIndex2 = 1;
showSlides2(slideIndex2)

function plusSlides2(n){
    showSlides2(slideIndex2 += n)
}
function currentSlide2(n){
    showSlides2(slideIndex2 = n)
}
function showSlides2(n){
    let i;
    let slides = document.querySelectorAll(".mySlides2");
    let quadrates = document.querySelectorAll(".quadrate2"); 
    if(n > slides.length) slideIndex2 = 1
    if(n < 1) slideIndex2 = slides.length
    for(i = 0; i < slides.length; i++){
        slides[i].style.display = "none"
    }
    for(i = 0; i < quadrates.length;i++){
        quadrates[i].className = quadrates[i].className.replace("active-carousel","")
    }
    slides[slideIndex2-1].style.display = "block";
    quadrates[slideIndex2-1].className += " active-carousel";
}

// carousel 3
let slideIndex3 = 1;
showSlides3(slideIndex3)

function plusSlides3(n){
    showSlides3(slideIndex3 += n)
}
function currentSlide3(n){
    showSlides3(slideIndex3 = n)
}
function showSlides3(n){
    let i;
    let slides = document.querySelectorAll(".mySlides3");
    let quadrates = document.querySelectorAll(".quadrate3"); 
    if(n > slides.length) slideIndex3 = 1
    if(n < 1) slideIndex3 = slides.length
    for(i = 0; i < slides.length; i++){
        slides[i].style.display = "none"
    }
    for(i = 0; i < quadrates.length;i++){
        quadrates[i].className = quadrates[i].className.replace("active-carousel3","")
    }
    slides[slideIndex3-1].style.display = "block";
    quadrates[slideIndex3-1].className += " active-carousel3";
}


// ventana emergente para Evento Club Nocturno
const ventanaEmergenteCNocturno = document.getElementById("ventanaEmergenteCNocturno"),
    openButtoncNocturno = document.getElementById("open-button-cNocturno"),
    closeButtoncNocturno = document.getElementById("close-button-cNocturno");

openButtoncNocturno.addEventListener("click", () => {
    ventanaEmergenteCNocturno.style.display = "flex";
    document.body.style.overflow = "hidden";
});

closeButtoncNocturno.addEventListener("click", () => {
    ventanaEmergenteCNocturno.style.display = "none";
    document.body.style.overflow = "auto";
});

// ventana emergente para Evento Piano Bar
const ventanaEmergentePBar = document.getElementById("ventanaEmergentePBar"),
    openButtoncPBar = document.getElementById("open-button-PBar"),
    closeButtoncPBar = document.getElementById("close-button-PBar");

    openButtoncPBar.addEventListener("click", () => {
    ventanaEmergentePBar.style.display = "flex";
    document.body.style.overflow = "hidden";
});

closeButtoncPBar.addEventListener("click", () => {
    ventanaEmergentePBar.style.display = "none";
    document.body.style.overflow = "auto";
});

// ventana emergente para Evento Salon Diversion
const ventanaEmergenteSDiversion = document.getElementById("ventanaEmergenteSDiversion"),
    openButtoncSDiversion = document.getElementById("open-button-SDiversion"),
    closeButtoncSDiversion = document.getElementById("close-button-SDiversion");

    openButtoncSDiversion.addEventListener("click", () => {
    ventanaEmergenteSDiversion.style.display = "flex";
    document.body.style.overflow = "hidden";
});

closeButtoncSDiversion.addEventListener("click", () => {
    ventanaEmergenteSDiversion.style.display = "none";
    document.body.style.overflow = "auto";
});


// ventana emergente para Evento Salon Diversion
const ventanaEmergenteSReunion = document.getElementById("ventanaEmergenteSReunion"),
    openButtoncSReunion = document.getElementById("open-button-SReunion"),
    closeButtoncSReunion = document.getElementById("close-button-SReunion");

    openButtoncSReunion.addEventListener("click", () => {
    ventanaEmergenteSReunion.style.display = "flex";
    document.body.style.overflow = "hidden";
});

closeButtoncSReunion.addEventListener("click", () => {
    ventanaEmergenteSReunion.style.display = "none";
    document.body.style.overflow = "auto";
});