// const data={{ books_json|safe }}; // Виведе дані книг у форматі JSON з Django

document.addEventListener('DOMContentLoaded', function() {
    const booksDataElement = document.getElementById('books-data');
    if (booksDataElement) {
        console.log(data[1]);  // Виведе "Book 1"
        console.log(data[0]['fields']['title']);  // Виведе "Book 1"
        console.log(data[0].fields.title);  // Виведе "Book 1"
    } else {
        console.error('Елемент з id "books-data" не знайдений');
    }
});

const tableBody = document.querySelector('tbody');
const filterInput = document.getElementById('filterInput');
const sortButton = document.getElementById('sortButton');

let isDescending = true;

// Функція для підсвічування
function highlight(text, query) {
    if (typeof text !== 'string') {
        // console.error('Помилка: text не є рядком:', text);
        return text.toString(); // Повертаємо незмінене значення
    }
    if (!query) return text; // Якщо немає пошукового запиту, повертаємо текст без змін
    const regex = new RegExp(`(${query})`, 'gi'); // Регулярний вираз для пошуку
    return text.replace(regex, '<span class="highlight">$1</span>'); // Обгортаємо знайдене в <span>
}

// Функція для рендерингу таблиці з підсвічуванням
function renderTable(filteredBooks, query) {
    tableBody.innerHTML = ''; // Очищаємо таблицю
    filteredBooks.forEach(book => {
        const bookf = book['fields']; // Дістаємо дані книги
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><a href="/books/table/${bookf['num']}">${highlight(bookf['num'].toString(), query)}</a></td>
            <td><a href="/books/table/${bookf['num']}">${highlight(bookf['title'], query)}</a></td>
            <td>${highlight(bookf['author'], query)}</td>
            <td><a href="/books/table/category/${bookf['category']}">${highlight(bookf['category'], query)}</a></td>
            <td><a href="/books/table/subcategory/${bookf['subcategory']}">${highlight(bookf['subcategory'], query)}</a></td>
        `;
        tableBody.appendChild(row);
    });
}

// !! Книги, що з однаковим номером
// x = 1;
// for (let i = 0; i < data.length; i++) {
//     if (data[i]['fields']['num'] === x) {
//         console.log(data[i]['fields']['num']);
//     }
//     x = data[i]['fields']['num'];
// }

// Початкове рендерингу таблиці
renderTable(data, '');

// Додаємо подію для фільтру
filterInput.addEventListener('input', () => {
    const filterValue = filterInput.value.toLowerCase();
    const filteredBooks = data.filter(book =>
        book['fields']['num'].toString().includes(filterValue) || 
        book['fields']['title'].toLowerCase().includes(filterValue) ||
        book['fields']['author'].toLowerCase().includes(filterValue) ||
        book['fields']['category'].toLowerCase().includes(filterValue) ||
        book['fields']['subcategory'].toLowerCase().includes(filterValue)
    );
    renderTable(filteredBooks, filterValue); // Передаємо фільтрований список і запит для підсвічування
});

sortButton.addEventListener('click', () => {
    const sortedBooks = [...data].sort((a, b) => {
        if (isDescending) {
            return b['fields']['num'] - a['fields']['num']; // Сортування за спаданням
        } else {
            return a['fields']['num'] - b['fields']['num']; // Сортування за зростанням
        }
    });
    
    isDescending = !isDescending; // Змінюємо порядок сортування

    const filterValue = filterInput.value.toLowerCase();
    renderTable(sortedBooks.filter(book => 
        book['fields']['num'].toString().includes(filterValue) ||
        book['fields']['title'].toLowerCase().includes(filterValue) ||
        book['fields']['author'].toLowerCase().includes(filterValue) ||
        book['fields']['category'].toLowerCase().includes(filterValue) ||
        book['fields']['subcategory'].toLowerCase().includes(filterValue) 
    ), filterValue);
});

