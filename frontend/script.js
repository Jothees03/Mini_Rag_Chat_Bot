const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");

async function sendMessage() {
    const question = input.value.trim();
    if (!question) return;

    // User message
    addMessage(question, "user");
    input.value = "";

    // Thinking message
    const thinking = addMessage("Thinking...", "bot");

    try {
        const response = await fetch("http://127.0.0.1:3448/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        // Remove thinking
        chatBox.removeChild(thinking);

        const botMsg = document.createElement("div");
        botMsg.className = "message bot";
        botMsg.innerHTML = `
            ${data.answer}
            <div class="source">${data.source}</div>
        `;
        chatBox.appendChild(botMsg);

    } catch (err) {
        chatBox.removeChild(thinking);
        addMessage("❌ Error connecting to server", "bot");
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

function addMessage(text, type) {
    const msg = document.createElement("div");
    msg.className = `message ${type}`;
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
    return msg;
}

// Enter key support
input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
