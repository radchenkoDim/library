document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");
    const content = document.getElementById("main-content");
    // const content = document.querySelector(".content");
    // const listBooks = document.querySelector(".list-books");
    // console.log(listBooks);

    toggleButton.addEventListener("click", function () {
        menu.classList.toggle("active");
        content.classList.toggle("non_active");
        // content.classList.toggle("non_active");
        // listBooks.classList.toggle("non_active");
    });

    document.addEventListener("click", function (event) {
    if (!menu.contains(event.target) && !toggleButton.contains(event.target)) {
        menu.classList.remove("active");
        content.classList.remove("non_active");
        // content.classList.remove("non_active");
        // listBooks.classList.remove("active");
    }
    });
});