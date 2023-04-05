window.addEventListener("load", solve);

function solve() {
  const formInputs = {
    title: document.getElementById("post-title"),
    category: document.getElementById("post-category"),
    content: document.getElementById("post-content")
  }

  const formValues = {}
  let postId = 0;
  const publishBtn = document.getElementById("publish-btn");
  publishBtn.addEventListener("click", publishHandler);
  const clearBtn = document.getElementById("clear-btn");
  clearBtn.addEventListener("click", clearHandler);

  const reviewList = document.getElementById("review-list");
  const publishedList = document.getElementById("published-list");

  function publishHandler(e) {
    e.preventDefault();
    for (const element in formInputs) {
      if (formInputs[element].value === "") {
        return;
      }
    }
    let { title, category, content } = formInputs;
    let li = createDOMElement("li", reviewList, null, ["rpost"]);
    let article = createDOMElement("article", li);
    createDOMElement("h4", article, title.value);
    createDOMElement("p", article, `Category: ${category.value}`);
    createDOMElement("p", article, `Content: ${content.value}`);
    let editBtn = createDOMElement("button", li, "Edit", ["action-btn", "edit"], postId.toString());
    let approveBtn = createDOMElement("button", li, "Approve", ["action-btn", "approve"]);
    editBtn.addEventListener("click", editHandler);
    approveBtn.addEventListener("click", approveHandler);
    formValues[postId.toString()] = {
      title: title.value,
      category: category.value,
      content: content.value
    }
    for (const element in formInputs) {
      formInputs[element].value = "";

    }
    postId++;
  }
  

  function editHandler() {
    let id = this.id;
    let post = this.parentElement;
    formInputs.title.value = formValues[id.toString()].title;
    formInputs.category.value = formValues[id.toString()].category;
    formInputs.content.value = formValues[id.toString()].content;
    post.remove();
  }

  function approveHandler() {
    let post = this.parentElement;
    post.querySelector(".edit").remove();
    post.querySelector(".approve").remove();
    publishedList.appendChild(post);
  }

  function clearHandler() {
    publishedList.innerHTML = "";
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
