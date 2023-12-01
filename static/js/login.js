// Inicio de sesion
// Cambiar de seccion login a registrar
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});
sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});
// Icono de ojo para mostrar contraseña
const contraseñas = document.querySelectorAll(".pass");
const iconosOjo = document.querySelectorAll(".fa-eye");
iconosOjo.forEach((icono, index) => {
  icono.addEventListener("click", () => {
    // Comprueba si el input es de tipo password
    if (contraseñas[index].type === "password") {
      contraseñas[index].type = "text";
      icono.classList.remove("fa-eye");
      icono.classList.add("fa-eye-slash");
    } else {
      contraseñas[index].type = "password";
      icono.classList.remove("fa-eye-slash");
      icono.classList.add("fa-eye");
    }
  });
});

