function toggleChat() {
    const chatWindow = document.getElementById("chatWindow");
    if (chatWindow.style.display === "none" || chatWindow.style.display === "") {
        chatWindow.style.display = "block";
    } else {
        chatWindow.style.display = "none";
    }
  }