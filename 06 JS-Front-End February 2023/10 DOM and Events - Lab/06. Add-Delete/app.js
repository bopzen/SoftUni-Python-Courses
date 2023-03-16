function addItem() {
    let textInput = document.getElementById("newItemText").value;
    let newListElement = document.createElement("li");
    newListElement.appendChild(document.createTextNode(textInput));
    let newAnchor = document.createElement("a");
    newAnchor.textContent = "[Delete]";
    newAnchor.setAttribute('href', '#');
    newListElement.appendChild(newAnchor);
    document.getElementById("items").appendChild(newListElement);
    document.getElementById("newItemText").value = "";
    newAnchor.addEventListener("click", deleteHandler);

    function deleteHandler(e) {
        let anchor = e.currentTarget;
        console.log(anchor)
        anchor.parentElement.remove();
    }
}