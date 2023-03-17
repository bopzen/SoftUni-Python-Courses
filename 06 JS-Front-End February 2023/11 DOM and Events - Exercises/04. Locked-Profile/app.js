function lockedProfile() {
    let buttons = document.getElementsByTagName("button");
    for (const button of buttons) {
        button.addEventListener("click", onClick)
    }

    function onClick(e) {
        let element = e.currentTarget;
        let hiddenElement = element.parentElement.querySelector("div");
        let locked = element.parentElement.querySelector("input");
        if (element.textContent === "Show more") {
            if (!locked.checked) {
                element.textContent = "Hide it";
                hiddenElement.style.display = "block";
            }
        } else if (element.textContent === "Hide it") {
            if (!locked.checked) {
                element.textContent = "Show more";
                hiddenElement.style.display = "none";
            }
        }
    }
}