window.addEventListener("load", solve);

function solve() {
  const formElements = {
    firstName: document.getElementById("first-name"),
    lastName: document.getElementById("last-name"),
    age: document.getElementById("age"),
    gender: document.getElementById("genderSelect"),
    dishDescription: document.getElementById("task"),
  }

  let formInfo = {};
  let id = 1;
  const submitBtn = document.getElementById("form-btn");
  submitBtn.addEventListener("click", submitHandler);
  const clearBtn = document.getElementById("clear-btn");
  clearBtn.addEventListener("click", clearHandler);

  const inProgress = document.getElementById("in-progress");
  const progressCount = document.getElementById("progress-count");
  let dishesInProgress = 0;

  const finished = document.getElementById("finished");

  function submitHandler(e) {
    e.preventDefault();
    for (const element in formElements) {
      if (formElements[element].value == "") {
        return
      }
    }
    let {firstName, lastName, age, gender, dishDescription} = formElements;
    let li = createDOMElement("li", inProgress, null, ["each-line"]);
    let article = createDOMElement("article", li);
    createDOMElement("h4", article, `${firstName.value} ${lastName.value}`);
    createDOMElement("p", article, `${gender.value}, ${age.value}`);
    createDOMElement("p", article, `Dish description: ${dishDescription.value}`);
    let editBtn = createDOMElement("button", li, "Edit", ["edit-btn"], `${id}`);
    let markBtn = createDOMElement("button", li, "Mark as complete", ["complete-btn"]);
    editBtn.addEventListener("click", editHandler);
    markBtn.addEventListener("click", markHandler);

    formInfo[`${id}`] = {
      firstName: firstName.value, 
      lastName: lastName.value,
      age: age.value,
      gender: gender.value,
      dishDescription: dishDescription.value
    };
    id++;
    for (const element in formElements) {
      
      formElements[element].value = "";
    }
    id++;
    dishesInProgress++;
    progressCount.textContent = dishesInProgress;

  }

  function editHandler() {
    let info = this.parentElement;
    formElements.firstName.value = formInfo[this.id].firstName;
    formElements.lastName.value = formInfo[this.id].lastName;
    formElements.age.value = formInfo[this.id].age;
    formElements.gender.value = formInfo[this.id].gender;
    formElements.dishDescription.value = formInfo[this.id].dishDescription;

    info.remove();
    dishesInProgress--;
    progressCount.textContent = dishesInProgress;
  }

  function markHandler() {
    let info = this.parentElement;
    let editBtn = info.querySelector(".edit-btn");
    let markBtn = info.querySelector(".complete-btn");
    editBtn.remove();
    markBtn.remove();
    finished.appendChild(info);
    dishesInProgress--;
    progressCount.textContent = dishesInProgress;
  }

  function clearHandler() {
    finished.innerHTML = "";
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
