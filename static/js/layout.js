document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");
    const content = document.getElementById("main-content");
    const homeLink = document.getElementById("home-link");

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

    function updateMenuLinks() {
        if (window.innerWidth < 768) {
            homeLink.innerHTML = "бібліотека";

            if (!document.getElementById("sign-up-link")) {
                const signUpLink = document.createElement("a");
                signUpLink.href = "/users/register/";
                signUpLink.classList.add("head-link");
                signUpLink.id = "sign-up-link";
                signUpLink.innerHTML = "зареєструватись";
                menu.appendChild(signUpLink);
            }
        } else {
            homeLink.innerHTML = "головна";
            const signUpLink = document.getElementById("sign-up-link");
            if (signUpLink) {
                menu.removeChild(signUpLink);
            }
        }
    }

    updateMenuLinks();
    window.addEventListener("resize", updateMenuLinks);
    
    // transmitted through the html head tag
    if (user.is_authenticated) {
        const signUpLink = document.getElementById("sign-up-link");
        if (signUpLink) {
            menu.removeChild(signUpLink);
        }
    }
});