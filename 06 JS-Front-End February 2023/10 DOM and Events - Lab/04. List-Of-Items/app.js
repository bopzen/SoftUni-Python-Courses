function addItem() {
    let textInput = document.getElementById("newItemText").value;
    let newListElement = document.createElement("li");
    newListElement.appendChild(document.createTextNode(textInput));
    document.getElementById("items").appendChild(newListElement);
    document.getElementById("newItemText").value = "";
}