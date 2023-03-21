function validate() {
    let input = document.getElementById("email");
    input.addEventListener("change", changeHandler);

    function changeHandler(event) {
        let inputEmail = input.value;
        let regex = /[a-z]+[@{1}][a-z]+[.{1}][a-z]+/gm

        let checkedEmail = regex.test(inputEmail);
        console.log(inputEmail)
        console.log(checkedEmail)
        if (!checkedEmail) {
            input.classList.add("error");
        } else {
            input.classList.remove("error");
        }
    }
}