document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");
    const content = document.querySelector(".content");

    toggleButton.addEventListener("click", function () {
        menu.classList.toggle("active");
        content.classList.toggle("non_active");
    });

    document.addEventListener("click", function (event) {
    if (!menu.contains(event.target) && !toggleButton.contains(event.target)) {
        menu.classList.remove("active");
        content.classList.remove("non_active");
    }
    });
});