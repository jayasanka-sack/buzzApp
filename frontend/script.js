const socket = io();
const username = prompt("What's your name?"); 
let alternate = false;

document.getElementById("message").addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

const sendMessage = () => {
    const messageInput = document.getElementById("message");
    const data = {
        username: username,
        message: messageInput.value
    };
    socket.emit("send_message", data);
    messageInput.value = '';
};
socket.on("new_message", (data) => {
    const messagesBox = document.getElementById("messages");
    const messageClass = data.username === username ? 'self' : (alternate ? 'alternate' : '');
    alternate = !alternate;

    const messageHtml = `<div class="message ${messageClass}">${data.username}: ${data.message}</div>`;
    messagesBox.innerHTML += messageHtml;
    messagesBox.scrollTop = messagesBox.scrollHeight;
});
