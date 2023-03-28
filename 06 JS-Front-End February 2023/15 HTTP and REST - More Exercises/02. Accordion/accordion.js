function solution() {
    const BASE_URL = "http://localhost:3030/jsonstore/advanced/articles/";
    let main = document.getElementById("main");
    loadArticles();

    async function loadArticles() {
        const response = await fetch(`${BASE_URL}list`);
        const data = await response.json();
        for (const {_id, title} of data) {
            let newAccordion = document.createElement("div");
            newAccordion.classList.add("accordion");

            let newHead = document.createElement("div");
            newHead.classList.add("head");


            let newSpan = document.createElement("span");
            newSpan.textContent = title;
            
            let button = document.createElement("button");
            button.classList.add("button");
            button.id = _id;
            button.textContent = "More";
            button.addEventListener("click", clickHandler);

            newHead.appendChild(newSpan);
            newHead.appendChild(button);
            newAccordion.appendChild(newHead);
            main.appendChild(newAccordion);
        }
    }

    async function clickHandler(event) {
        let button = event.currentTarget;
        if (button.textContent == "More") {
            let response = await fetch(`http://localhost:3030/jsonstore/advanced/articles/details/${button.id}`);
            let data = await response.json();
            
            let newExtra = document.createElement("div");
            newExtra.classList.add("extra");
            let newP = document.createElement("p");
            newP.textContent = data.content;
            newExtra.appendChild(newP);
            button.parentElement.parentElement.appendChild(newExtra);
            newExtra.style.display = "block";
            button.textContent = "Less";
        } else {
            button.parentElement.parentElement.removeChild(button.parentElement.parentElement.lastElementChild);
            button.textContent = "More";
        }
    }
}

solution();