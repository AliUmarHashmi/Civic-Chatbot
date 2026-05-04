function sendMessage() {
    let inputField = document.getElementById("userInput");
    let message = inputField.value.trim();

    if (message === "") return;

    let chatbox = document.getElementById("chatbox");

    let userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.innerText = message;
    chatbox.appendChild(userMsg);

    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        let botMsg = document.createElement("div");
        botMsg.className = "message bot";
        botMsg.innerText = data.response;

        chatbox.appendChild(botMsg);
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    inputField.value = "";
}