function focused() {
    let inputFields = document.getElementsByTagName("input");
    for (const inputField of inputFields) {
        inputField.addEventListener("focus", inFocus);
        inputField.addEventListener("blur", outFocus);
    } 
    function inFocus(e) {
        let element = e.currentTarget;
        element.parentElement.className = "focused";
        console.log(element)
    }
    function outFocus(e) {
        let element = e.currentTarget;
        element.parentElement.classList.remove("focused");
        console.log(element)
    }
        
    console.log(inputFields)
}