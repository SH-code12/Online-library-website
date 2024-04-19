

function show_message(book){
    var message = document.getElementById("message-box");
    var messageText = document.getElementById('message-text');
    messageText.innerText =  book;
    message.style.display = "block";
}

function hide_Message(){
    var message = document.getElementById("message-box");
    message.style.display = "none";
}



