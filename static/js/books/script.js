// const data={{ books_json|safe }}; // Виведе дані книг у форматі JSON з Django

const tableBody = document.querySelector('tbody');
const filterInput = document.getElementById('filterInput');
const sortButton = document.getElementById('sortButton');

let isDescending = true;

function highlight(text, query) {
    if (typeof text !== 'string') {

        return text.toString();
    }
    if (!query) return text; 
    const regex = new RegExp(`(${query})`, 'gi'); 
    return text.replace(regex, '<span class="highlight">$1</span>'); 
}

// Функція для рендерингу таблиці з підсвічуванням
function renderTable(filteredBooks, query) {
    tableBody.innerHTML = '';

    if (filteredBooks.length === 0) {
        const row = document.createElement('tr');
        row.innerHTML = '<td colspan="4">Нічого не знайдено</td>';
        tableBody.appendChild(row);
        return;
    }

    filteredBooks.forEach(book => {
        const bookf = book['fields'];
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><a href="/books/table/${bookf['num']}">${highlight(bookf['num'].toString(), query)}</a></td>
            <td><a href="/books/table/${bookf['num']}">${highlight(bookf['title'], query)}</a></td>
            <td><a href="/books/table/author/${bookf['author']}">${highlight(bookf['author'], query)}</td>
            <td><a href="/books/table/category/${bookf['category']}">${highlight(bookf['category'], query)}</a></td>
        `;
        tableBody.appendChild(row);
    });
}

// Функція для фільтрування книг
function filterBooks(query) {
    return data.filter(book => {
        const bookf = book['fields'];
        return (
            bookf['num']?.toString().includes(query) ||
            bookf['title']?.toLowerCase().includes(query) ||
            bookf['author']?.toLowerCase().includes(query) ||
            bookf['category']?.toLowerCase().includes(query)
        );
    });
}

// Додаємо подію для фільтру
filterInput.addEventListener('input', () => {
    const filterValue = filterInput.value.toLowerCase();
    const filteredBooks = filterBooks(filterValue);
    renderTable(filteredBooks, filterValue);
});

// sortButton.addEventListener('click', () => {
//     const sortedBooks = [...data].sort((a, b) => {
//         if (isDescending) {
//             return b['fields']['num'] - a['fields']['num']; // Сортування за спаданням
//         } else {
//             return a['fields']['num'] - b['fields']['num']; // Сортування за зростанням
//         }
//     });
    
//     isDescending = !isDescending; // Змінюємо порядок сортування

//     const filterValue = filterInput.value.toLowerCase();
//     renderTable(sortedBooks.filter(book => 
//         book['fields']['num'].toString().includes(filterValue) ||
//         book['fields']['title'].toLowerCase().includes(filterValue) ||
//         book['fields']['author'].toLowerCase().includes(filterValue) ||
//         book['fields']['category'].toLowerCase().includes(filterValue) 
//     ), filterValue);
// });

