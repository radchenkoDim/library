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
        row.innerHTML = '<td colspan="3">Нічого не знайдено</td>';
        tableBody.appendChild(row);
        return;
    }

    filteredBooks.forEach(book => {
        const bookf = book['fields'];
        const fileUrl = bookf['file'];
        console.log(fileUrl);
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><a href="/media/${bookf['file']}" target="_blanck">${highlight(bookf['title'], query)}</a></td>
            <td>${highlight(bookf['author'], query)}</td>
            <td>${highlight(bookf['category'], query)}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Функція для фільтрування книг
function filterBooks(query) {
    return data.filter(book => {
        const bookf = book['fields'];
        return (
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
  