function attachEvents() {
    const BASE_URL = "http://localhost:3030/jsonstore/phonebook/";
    let phonebookContainer = document.getElementById("phonebook");
    let loadBtn = document.getElementById("btnLoad");
    let createBtn = document.getElementById("btnCreate");
    let inputPerson = document.getElementById("person");
    let inputPhone = document.getElementById("phone");

    loadBtn.addEventListener("click", loadHandler);
    createBtn.addEventListener("click", createHandler);
    deleteBtn.addEventListener("click", deleteHandler);

    async function loadHandler() {
        try {
            phonebookContainer.innerHTML = "";
            const response = await fetch(`${BASE_URL}`);
            const data = await response.json();
            let phonesList = Object.values(data);
            for (const {person, phone, _id} of phonesList) {
                let newLi = document.createElement("li");
                newLi.textContent = `${person}: ${phone}`;
                let newDeleteBtn = document.createElement("button");
                newDeleteBtn.textContent = "Delete";
                newDeleteBtn.id = _id;
                newDeleteBtn.addEventListener("click", deleteHandler);
                newLi.appendChild(newDeleteBtn);
                phonebookContainer.appendChild(newLi);
            }
        }
        catch (error) {
            console.log(error);
        }
    }

    async function createHandler() {
        try {
            let newEntry = {
                person: inputPerson.value,
                phone: inputPhone.value
            }
            const httpHeaders = {
                method: "post",
                body: JSON.stringify(newEntry)
            }
            const resData = await fetch(`${BASE_URL}`, httpHeaders);
            loadHandler();
        }
        catch (error) {
            console.log(error);
        }
    }

    async function deleteHandler(e) {
        try {
            const id = this.id;
            const httpHeaders = {
                method: "delete"
            };
            const resData = await fetch(`${BASE_URL}${id}`, httpHeaders);
            loadHandler();
        }
        catch (error) {
            console.log(error);
        }
    }
}

attachEvents();