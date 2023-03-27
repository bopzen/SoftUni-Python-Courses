function attachEvents() {
  const BASE_URL = "http://localhost:3030/jsonstore/collections/books/";
  let formHeader = document.querySelector("#form h3");
  let loadBooksBtn = document.getElementById("loadBooks");
  let booksTable = document.getElementsByTagName("tbody")[0];
  let [inputTitle, inputAuthor] = Array.from(document.querySelectorAll("#form input"));
  let submitBtn = document.querySelector("#form button");
  let bookId;
  loadBooksBtn.addEventListener("click", loadHandler);
  submitBtn.addEventListener("click", submitHandler)

  async function loadHandler() {
    try {
      booksTable.innerHTML = "";
      let response = await fetch(BASE_URL);
      let data = await response.json();
      console.log(data)
      for (const bookId in data) {
        let newRow = document.createElement("tr");
        newRow.id = bookId;
  
        let td = document.createElement("td");
        td.textContent = data[bookId]["title"];
        newRow.appendChild(td);
  
        td = document.createElement("td");
        td.textContent = data[bookId]["author"];
        newRow.appendChild(td);
  
        td = document.createElement("td");
        editBtn = document.createElement("button");
        editBtn.textContent = "Edit";
        editBtn.addEventListener("click", editHandler);
        deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.addEventListener("click", deleteHandler);
        td.appendChild(editBtn);
        td.appendChild(deleteBtn);
        newRow.appendChild(td);
  
        booksTable.appendChild(newRow);
      }
    }
    catch (error) {
      console.log(error);
    }
  }

  function editHandler(event) {
    try {
      formHeader.textContent = "Edit FORM";
      submitBtn.textContent = "Save";
      bookId = event.currentTarget.parentElement.parentElement.id;
      let title = event.currentTarget.parentElement.parentElement.children[0].textContent;
      let author = event.currentTarget.parentElement.parentElement.children[1].textContent;
      inputTitle.value = title;
      inputAuthor.value = author
    }
    catch (error) {
      console.log(error);
    }
  }

  async function deleteHandler(event) {
    try {
      let bookId = event.currentTarget.parentElement.parentElement.id;
      let httpHeader = {
        method: "delete"
      }
      await fetch(`${BASE_URL}${bookId}`, httpHeader);
      loadHandler();
    }
    catch (error) {
      console.log(error);
    }
  }

  async function submitHandler() {
    try {
      let newBook = {
        title: inputTitle.value,
        author: inputAuthor.value
      }
      let httpHeader = {
        method: "post",
        body: JSON.stringify(newBook)
      }
      let url = BASE_URL;
      if (submitBtn.textContent === "Save") {
        httpHeader.method = "put";
        url = BASE_URL + bookId;
      }
      await fetch(url, httpHeader);
      if (formHeader.textContent === "Edit FORM") {
        formHeader.textContent = "FORM";
        submitBtn.textContent = "Submit";
      }
      inputTitle.value = "";
      inputAuthor.value = "";
      loadHandler();
    }
    catch (error) {
      console.log(error);
    }
  }

}

attachEvents();