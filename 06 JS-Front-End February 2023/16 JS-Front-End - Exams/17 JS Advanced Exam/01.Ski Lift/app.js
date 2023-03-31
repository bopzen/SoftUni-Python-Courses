window.addEventListener('load', solve);

function solve() {
    const inputElements = {
        firstName: document.getElementById("first-name"),
        lastName: document.getElementById("last-name"),
        peopleCount: document.getElementById("people-count"),
        fromDate: document.getElementById("from-date"),
        daysCount: document.getElementById("days-count"),      
    }

    const inputData = {};
    let nextBtn = document.getElementById("next-btn");
    nextBtn.addEventListener("click", nextHandler);
    
    let body = document.getElementById("body");
    let main = document.getElementById("main");
    let ticketPreview = document.querySelector(".ticket-info-list");
    let ticketConfirm = document.querySelector(".confirm-ticket");

    function nextHandler(event) {
        event.preventDefault();
        for (const inputElement of Object.values(inputElements)) {
            if (inputElement.value === "") {
                return;
            }
        }
        let li = createDOMElement("li", ticketPreview, null, ["ticket"]);
        let article = createDOMElement("article", li);
        createDOMElement("h3", article, `Name: ${inputElements.firstName.value} ${inputElements.lastName.value}`)
        createDOMElement("p", article, `From date: ${inputElements.fromDate.value}`);
        createDOMElement("p", article, `For ${inputElements.daysCount.value} days`);
        createDOMElement("p", article, `For ${inputElements.peopleCount.value} people`);
        let editBtn = createDOMElement("button", li, "Edit", ["edit-btn"]);
        let continueBtn = createDOMElement("button", li, "Continue", ["continue-btn"]);
        editBtn.addEventListener("click", editHandler);
        continueBtn.addEventListener("click", continueHandler);

        for (const key in inputElements) {
            inputData[key] = inputElements[key].value;
            inputElements[key].value = ""
        }

        nextBtn.setAttribute("disabled", true);
    }

    function editHandler() {
        this.parentElement.remove();
        for (const key in inputData) {
            inputElements[key].value = inputData[key];
        }
        nextBtn.removeAttribute("disabled");
    }

    function continueHandler() {
        let ticketData = this.parentElement;       
        let editBtn = ticketData.querySelector(".edit-btn");
        let continueBtn = ticketData.querySelector(".continue-btn");
        let confirmBtn = createDOMElement("button", ticketData, "Confirm", ["confirm-btn"]);
        let cancelBtn = createDOMElement("button", ticketData, "Cancel", ["cancel-btn"]);
        confirmBtn.addEventListener("click", confirmHandler);
        cancelBtn.addEventListener("click", cancelHandler);
        ticketConfirm.appendChild(ticketData);
        editBtn.remove();
        continueBtn.remove();
    }

    function confirmHandler() {
        main.remove();
        createDOMElement("h1", body, "Thank you, have a nice day!", null, "thank-you");
        let backBtn = createDOMElement("button", body, "Back", null, "back-btn");
        backBtn.addEventListener("click", backHandler);
    }

    function cancelHandler() {
        this.parentElement.remove();
        nextBtn.removeAttribute("disabled");
    }

    function backHandler() {
        window.location.reload();
    }

    function createDOMElement(type, parentElement, content, classes, id, attributes, useInnerHTML) {
        const newElement = document.createElement(type);
    
        if (content && useInnerHTML) {
          newElement.innerHTML = content;
        } else {
          if (content && type !== "input") {
            newElement.textContent = content;
          }
          if (content && type === "input") {
            newElement.value = content;
          }
        }
    
        if (classes && classes.length > 0) {
          newElement.classList.add(...classes);
        }
    
        if (id) {
          newElement.id = id;
        }
    
        if (attributes) {
          for (const key in attributes) {
            newElement[key] = attributes[key];
          }
        }
    
        if (parentElement) {
          parentElement.appendChild(newElement);
        }
        return newElement;
      
    }
}
