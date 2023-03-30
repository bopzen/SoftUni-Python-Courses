window.addEventListener("load", solve);

function solve() {
  let inputFields = {}
  let inputFieldsValues = {
  };
  inputFields.firstName = document.getElementById("first-name");
  inputFields.lastName = document.getElementById("last-name");
  inputFields.age = document.getElementById("age");
  inputFields.storyTitle = document.getElementById("story-title");
  inputFields.genre = document.getElementById("genre");
  inputFields.story = document.getElementById("story");
  let previewContainer = document.getElementById("preview-list");
  let mainContainer = document.getElementById("main");

  publishBtn = document.getElementById("form-btn");
  publishBtn.addEventListener("click", publishHandler);


  function publishHandler() {
    for (const inputField in inputFields) {
      if (inputFields[inputField].value == "") {
        return;
      }
    }
    const {firstName, lastName, age, storyTitle, genre, story} = inputFields;
    const li = createDOMElement("li", previewContainer, null, ["story-info"]);
    const article = createDOMElement("article", li);
    createDOMElement("h4", article, `Name: ${firstName.value} ${lastName.value}`);
    createDOMElement("p", article, `Age: ${age.value}`);
    createDOMElement("p", article, `Title: ${storyTitle.value}`);
    createDOMElement("p", article, `Genre: ${genre.value}`);
    createDOMElement("p", article, story.value);
    const saveBtn = createDOMElement("button", li, "Save Story", ["save-btn"]);
    const editBtn = createDOMElement("button", li, "Edit Story", ["edit-btn"]);
    const deleteBtn = createDOMElement("button", li, "Delete Story", ["delete-btn"]);
    saveBtn.addEventListener("click", saveHandler);
    editBtn.addEventListener("click", editHandler);
    deleteBtn.addEventListener("click", deleteHandler);

    for (const inputField in inputFields) {
      inputFieldsValues[inputField] = inputFields[inputField].value;
      inputFields[inputField].value = "";
    }

    publishBtn.setAttribute("disabled", true);
  }

  function saveHandler() {
    mainContainer.innerHTML = "";
    createDOMElement("h1", mainContainer, "Your scary story is saved!");
  }

  function editHandler() {
    for (const inputField in inputFields) {
      inputFields[inputField].value = inputFieldsValues[inputField]
    }
    previewContainer.innerHTML = "";
    createDOMElement("h3", previewContainer, "Preview");
    publishBtn.removeAttribute("disabled");
  }

  function deleteHandler() {
    previewContainer.innerHTML = "";
    createDOMElement("h3", previewContainer, "Preview");
    publishBtn.removeAttribute("disabled");
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
