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

for (let i = 0; i < 10; i++) {
    let dataItem = data[i]['fields']
    console.log(
        dataItem['num'],
        dataItem['title'],
        dataItem['author'],
        dataItem['category'],
        dataItem['subcategory'],
        dataItem['year'],
        dataItem['tom'],
        dataItem['publisher'],
        dataItem['notes']
    )
}

