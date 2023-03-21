function solve() {
    let select = document.getElementById("selectMenuTo");
    select.children[0].value = "binary";
    select.children[0].textContent = "Binary";
    let newOption = document.createElement("option");
    newOption.value = "hexadecimal";
    newOption.textContent = "Hexadecimal"
    select.appendChild(newOption);

    let button = document.getElementsByTagName("button")[0];
    button.addEventListener("click", clickHandler);

    function clickHandler() {
        let input = Number(document.getElementById("input").value);
        let result = document.getElementById("result");
        let convertOption = select.options[select.selectedIndex].value;
        if (convertOption === "binary") {
            result.value = input.toString(2);
        } else if (convertOption === "hexadecimal") {
            result.value = input.toString(16).toUpperCase();
        }
    }
}