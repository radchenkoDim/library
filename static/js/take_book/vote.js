document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".vote-button").forEach(button => {
        button.addEventListener("click", function() {
            let bookId = this.dataset.bookid;

            fetch(`/take_book/vote/${bookId}`, {})
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    const buttonContainer = document.getElementById(`vote-button-container-${bookId}`);
                    const voteButton = document.getElementById(`vote-${bookId}`);
                    let voteCount = document.getElementById(`votes-${bookId}`);
                    
                    voteButton.style.display = "none";
                    // if (voteButton) {
                    //     voteButton.style.transition = "opacity 0.5s ease-out"; // Додаємо анімацію
                    //     voteButton.style.opacity = "0"; // Плавно зменшуємо прозорість
                        
                    //     setTimeout(() => {
                    //         voteButton.style.display = "none"; // Ховаємо кнопку після анімації
                    //     }, 500); // Чекаємо 500 мс (час переходу)
                    // }
                    const newContainerContent = document.createElement("p");
                    newContainerContent.innerHTML = "Ви вже проголосували";
                    buttonContainer.appendChild(newContainerContent);
                    voteCount.innerHTML = data.votes_count;
                }
            })
        });
    });
});