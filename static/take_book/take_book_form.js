const input_num = document.getElementById("id_book_num")
const placeholder = document.getElementById("book-placeholder")

if (input_num.value) {
    fetch(`/api/books/item/${input_num.value}/`)
        .then(function (response) {
            if (response.status !== 200) {
                throw new Error("Сталася помилка");
            }
            return response.json();
        })
        .then(function (data) {
            placeholder.innerText = data[0].fields.title;
            placeholder.style.color = "green";
            input_num.style.borderColor = "green";
        })
        .catch(function (error) {
            console.error("Щось пішло не так:", error);
        }
    );
}

input_num.addEventListener("input", function (event) {
    const value = event.target.value;

    placeholder.innerText = "";
    placeholder.style.color = "";
    input_num.style.borderColor = "";

    if (parseInt(value) > 0) {
        console.log(value);
        fetch(`/api/books/item/${value}/`)
            .then(function (response) {
                if (response.status !== 200) {

                    placeholder.innerText = "Книга не знайдена";
                    placeholder.style.color = "red";
                    input_num.style.borderColor = "red";

                    throw new Error("Сталася помилка");
                }
                return response.json();
            })
            .then(function (data) {
                placeholder.innerText = data[0].fields.title;
                placeholder.style.color = "green";
                input_num.style.borderColor = "green";
            })
            .catch(function (error) {
                console.error("Щось пішло не так:", error);
            });
    } else {
        document.getElementById("book-placeholder").innerText = "";
    }
});