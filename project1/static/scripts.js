async function sendPrompt() {
    const prompt = document.getElementById('prompt').value;
    if (!prompt.trim()) {
        alert("Please enter a description!");
        return;
    }

    const messagesContainer = document.getElementById('messages');

    // Add user message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.classList.add('message', 'user');
    userMessageDiv.innerHTML = `<strong>You:</strong> ${prompt}`;
    messagesContainer.appendChild(userMessageDiv);

    // Clear the input
    document.getElementById('prompt').value = '';

    // Scroll to bottom
    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description: prompt })
        });

        const result = await response.json();

        // Add bot message
        const botMessageDiv = document.createElement('div');
        botMessageDiv.classList.add('message', 'bot');
        botMessageDiv.innerHTML = `<strong>AI:</strong> ${result.code || result.error}`;
        messagesContainer.appendChild(botMessageDiv);

        // Scroll to bottom
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

    } catch (error) {
        const errorMessageDiv = document.createElement('div');
        errorMessageDiv.classList.add('message', 'bot');
        errorMessageDiv.innerHTML = `<strong>AI:</strong> Error generating code.`;
        messagesContainer.appendChild(errorMessageDiv);
    }
}
