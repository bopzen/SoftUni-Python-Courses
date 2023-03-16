function extractText() {
    let listLiItems = document.querySelectorAll("#items li");
    let text = document.querySelector("#result");
    for (const item of listLiItems) {
        text.value += item.textContent +"\n";
    }
}