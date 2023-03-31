window.addEventListener('load', solve);

function solve() {
    let inputElements = {
        firstName: document.getElementById("first-name"),
        lastName: document.getElementById("last-name"),
        dateIn: document.getElementById("date-in"),
        dateOut: document.getElementById("date-out"),
        numberOfGuests: document.getElementById("people-count")
    }

    let reservationInfoValues = {};
    let reservationInfo = document.querySelector(".info-list");
    let confirmReservation = document.querySelector(".confirm-list");
    let form = document.querySelector("form");
    let verification = document.getElementById("verification");

    let nextBtn = document.getElementById("next-btn");
    nextBtn.addEventListener("click", nextHandler);

    function nextHandler(event) {
        event.preventDefault();
        for (const key in inputElements) {
            if (inputElements[key].value === "") {
                return;
            }
        }
        const {firstName, lastName, dateIn, dateOut, numberOfGuests} = inputElements;
        if (dateIn.value > dateOut.value) {
            return;
        }
        let li = createDOMElement("li", reservationInfo, null, ["reservation-content"]);
        let article = createDOMElement("article", li);
        createDOMElement("h3", article, `Name: ${firstName.value} ${lastName.value}`);
        createDOMElement("p", article, `From date: ${dateIn.value}`);
        createDOMElement("p", article, `To date: ${dateOut.value}`);
        createDOMElement("p", article, `For ${numberOfGuests.value} people`);
        let editBtn = createDOMElement("button", li, "Edit", ["edit-btn"]);
        let continueBtn = createDOMElement("button", li, "Continue", ["continue-btn"]);
        editBtn.addEventListener("click", editHandler);
        continueBtn.addEventListener("click", continueHandler);

        reservationInfoValues = {
            firstName: firstName.value,
            lastName: lastName.value,
            dateIn: dateIn.value,
            dateOut: dateOut.value,
            numberOfGuests: numberOfGuests.value
        };

        form.reset();
        nextBtn.setAttribute("disabled", true);
    }

    function editHandler() {
        this.parentElement.remove();
        for (const key in reservationInfoValues) {
            inputElements[key].value = reservationInfoValues[key];
        }
        nextBtn.removeAttribute("disabled");
    }

    function continueHandler() {
        let reservation = this.parentElement;
        let editBtn = reservation.querySelector(".edit-btn");
        let continueBtn = reservation.querySelector(".continue-btn");
        let confirmBtn = createDOMElement("button", reservation, "Confirm", ["confirm-btn"]);
        let cancelBtn = createDOMElement("button", reservation, "Cancel", ["cancel-btn"]);
        confirmBtn.addEventListener("click", confirmHandler);
        cancelBtn.addEventListener("click", cancelHandler);
        editBtn.remove();
        continueBtn.remove();
        confirmReservation.appendChild(reservation);
    }

    function confirmHandler() {
        this.parentElement.remove();
        verification.classList.add("reservation-confirmed");
        verification.textContent = "Confirmed."
        nextBtn.removeAttribute("disabled");
    }

    function cancelHandler() {
        this.parentElement.remove();
        verification.classList.add("reservation-cancelled");
        verification.textContent = "Cancelled."
        nextBtn.removeAttribute("disabled");
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




    
    
