// Eng:Shahd Elnassag ^_^

function displayBooksTable() {
    let booksTableBody = document.getElementById('booksTableBody');
    booksTableBody.innerHTML = ''; // Clear previous content

    books.forEach(function(book) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${book.id}</td>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.category}</td>
            <td>${book.description}</td>
            <td>${book.status}</td>
        `;
        booksTableBody.appendChild(row);
        
    });
}

window.addEventListener('DOMContentLoaded', function() {
    let storedBooks = localStorage.getItem('books');
    if (storedBooks) {
        books = JSON.parse(storedBooks);
    }
});


let books = [];


function displayBooks() {

    let booksContainer = document.getElementById('container');
    booksContainer.innerHTML = ''; 

    

    books.forEach(function(book) {

        let coverDiv = document.createElement('div');
        coverDiv.className = 'cover';

        let img = document.createElement('img');
        img.src = book.image;
        img.alt = book.title;

        let select = document.createElement('select');
        select.id = 'status-' + book.id;
        ['borrow', 'borrowed', 'not_in_library', 'read_only'].forEach(function(option) {
            let optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option.replace('_', ' ').toUpperCase();
            if (option === book.status) {
                optionElement.selected = true;
            }
            select.appendChild(optionElement);
        });

        let button = document.createElement('button');
        button.textContent = 'Update Status';
        button.addEventListener('click', function() {
            let status = document.getElementById('status-' + book.id).value;
            alert('Status of ' + book.status + ' is updated to: ' + status.toUpperCase());
        });

        coverDiv.appendChild(img);
        coverDiv.appendChild(select);
        coverDiv.appendChild(button);

        booksContainer.appendChild(coverDiv);
    });
}

function DisplayConfirmation(){
    let confirmationDiv = document.getElementById('confirm');
    confirmationDiv.innerText = 'Book added successfully!';
    confirmationDiv.style.display = 'block';
    setTimeout(function() {
        confirmationDiv.style.display = 'none';
    }, 3000);
}

function clearBookForm() {
    document.getElementById('id').value = '';
    document.getElementById('name').value = '';
    document.getElementById('author').value = '';
    document.getElementById('category').value = '';
    document.getElementById('Description').value = '';
    document.getElementById('image').value = '';
    document.getElementById('status').value = 'borrow'; // Reset the status to default value
}

function addBook() {
    let id = document.getElementById('id').value;
    let name = document.getElementById('name').value;
    let author = document.getElementById('author').value;
    let category = document.getElementById('category').value;
    let description = document.getElementById('Description').value;
    let image = document.getElementById('image').value;
    let status = document.getElementById('status').value;

    let newBook = {
        id: id,
        title: name,
        author: author,
        category: category,
        description: description,
        image: image,
        status: status
    };

    books.push(newBook);

    localStorage.setItem('books', JSON.stringify(books));

    DisplayConfirmation();

    clearBookForm(); 
}


document.addEventListener('submit', function(event) {
    event.preventDefault(); 
    addBook(); 
});


