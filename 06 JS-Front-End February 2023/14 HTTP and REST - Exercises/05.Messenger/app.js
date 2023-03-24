function attachEvents() {
    let [name, message] = document.querySelectorAll("div input");
    let submitBtn = document.getElementById("submit");
    let refreshBtn = document.getElementById("refresh");
    let textArea = document.getElementById("messages")
    submitBtn.addEventListener("click", submiHandler);
    refreshBtn.addEventListener("click", refreshHandler);

    async function submiHandler() {
        try {
            let newMessage = {author: name.value, content: message.value};
            console.log(newMessage)
            let httpHeaders = {
                method: "post",
                body: JSON.stringify(newMessage)
            }
            const resData = await fetch("http://localhost:3030/jsonstore/messenger", httpHeaders);
        }
        catch (error) {
            console.log(error);
        }
    }

    async function refreshHandler() {
        try {
            const response = await fetch("http://localhost:3030/jsonstore/messenger");
            const data = await response.json();
            let messages = Object.values(data);
            let messagesList = []
            for (const {author, content, _id} of messages) {
                messagesList.push(`${author}: ${content}`)
            }
            textArea.textContent = messagesList.join("\n");
        }
        catch (error) {
            console.log(error);
        }
    }

}

attachEvents();