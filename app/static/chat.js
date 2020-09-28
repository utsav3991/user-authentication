var client_id = Date.now()
document.querySelector("#ws-id").textContent = client_id;
var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
ws.onmessage = function (event) {
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    var content = document.createTextNode(event.data)
    message.appendChild(content)
    console.log(event.data)
    messages.appendChild(message)
};

function sendMessage(event) {
    event.preventDefault()
    var preview = document.getElementById("messageText")
    var file = document.querySelector('input[type=file]').files[0]
    const reader = new FileReader();

    reader.addEventListener("load", function () {
        preview.src = reader.result;
        // console.log(reader.result)
        ws.send(reader.result)
    }, false)

    if (file) {
        reader.readAsDataURL(file);
        // console.log(reader.readAsDataURL(file))
    }
    console.log(reader.result)
    preview.value = ''
    event.preventDefault()
}