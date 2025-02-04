const bookNumberInput = document.getElementById("id_book_num")
const placeholder = document.getElementById("book-placeholder")

if (bookNumberInput.value) {
    fetch(`/api/books/item/${bookNumberInput.value}/`)
        .then(function (response) {
            if (response.status !== 200) {
                throw new Error("Сталася помилка");
            }
            return response.json();
        })
        .then(data => {
            placeholder.innerText = data[0].fields.title;
            placeholder.style.color = "green";
            bookNumberInput.style.borderColor = "green";
        })
        .catch(error => {
            console.error("Щось пішло не так:", error);
        }
    );
}

bookNumberInput.addEventListener("input", event => {
    const value = event.target.value;

    placeholder.innerText = "";
    placeholder.style.color = "";
    bookNumberInput.style.borderColor = "";

    if (parseInt(value) > 0) {
        // console.log(value);
        fetch(`/api/books/item/${value}/`)
            .then(response => {
                if (response.status !== 200) {

                    placeholder.innerText = "Книга не знайдена";
                    placeholder.style.color = "red";
                    bookNumberInput.style.borderColor = "red";

                    throw new Error("Сталася помилка");
                }
                return response.json();
            })
            .then(data => {
                placeholder.innerText = data[0].fields.title;
                placeholder.style.color = "green";
                bookNumberInput.style.borderColor = "green";
            })
            .catch(error => {
                console.error("Щось пішло не так:", error);
            });
    } else {
        document.getElementById("book-placeholder").innerText = "";
    }
});