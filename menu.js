document.addEventListener("DOMContentLoaded", function () {
    const btMenu = document.querySelector(".bt-menu");
    const header = document.querySelector(".header");

    btMenu.addEventListener("click", function () {
        header.classList.toggle("menu-open");
    });
});



