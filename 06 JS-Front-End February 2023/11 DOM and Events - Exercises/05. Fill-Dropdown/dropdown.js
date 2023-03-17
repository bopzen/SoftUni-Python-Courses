function addItem() {
    let dropDown = document.getElementById("menu");
    let inputText = document.getElementById("newItemText");
    let inputValue = document.getElementById("newItemValue");
    let newOption = document.createElement("option");
    newOption.textContent = inputText.value;
    newOption.value = inputValue.value;
    inputText.value = "";
    inputValue.value = "";
    dropDown.appendChild(newOption);
}