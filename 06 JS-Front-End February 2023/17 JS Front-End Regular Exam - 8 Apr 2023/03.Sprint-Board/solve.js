function attachEvents() {
    const BASE_URL = "http://localhost:3030/jsonstore/tasks/";

    const loadBoardBtn = document.getElementById("load-board-btn");
    loadBoardBtn.addEventListener("click", loadBoardHandler);

    const inputTitle = document.getElementById("title");
    const inputDescription = document.getElementById("description");
    const createTaskBtn = document.getElementById("create-task-btn");
    createTaskBtn.addEventListener("click", createTaskHandler);

    const [toDoList, inProgressList, codeReviewList, doneList] = Array.from(document.querySelectorAll("#board-section article > ul"));

    async function loadBoardHandler() {
        toDoList.innerHTML = "";
        inProgressList.innerHTML = "";
        codeReviewList.innerHTML = "";
        doneList.innerHTML = "";
        let response = await fetch(BASE_URL);
        let data = await response.json();
        for (const task of Object.values(data)) {
            let li;
            if (task.status === "ToDo") {
                li = createDOMElement("li", toDoList, null, ["task"], task._id);
                createDOMElement("h3", li, task.title);
                createDOMElement("p", li, task.description);
                let taskBtn = createDOMElement("button", li, "Move to In Progress");
                taskBtn.addEventListener("click", moveToInProgressHandler);
            } else if (task.status === "In Progress") {
                li = createDOMElement("li", inProgressList, null, ["task"], task._id);
                createDOMElement("h3", li, task.title);
                createDOMElement("p", li, task.description);
                let taskBtn = createDOMElement("button", li, "Move to Code Review");
                taskBtn.addEventListener("click", moveToCodeReviewHandler);
            } else if (task.status === "Code Review") {
                li = createDOMElement("li", codeReviewList, null, ["task"], task._id);
                createDOMElement("h3", li, task.title);
                createDOMElement("p", li, task.description);
                let taskBtn = createDOMElement("button", li, "Move to Done");
                taskBtn.addEventListener("click", moveToDoneHandler);
            } else if (task.status === "Done") {
                li = createDOMElement("li", doneList, null, ["task"], task._id);
                createDOMElement("h3", li, task.title);
                createDOMElement("p", li, task.description);
                let taskBtn = createDOMElement("button", li, "Close");
                taskBtn.addEventListener("click", closeHandler);
            }
        }

    }

    async function moveToInProgressHandler() {
        let taskId = this.parentElement.id;
        let body = {
            status: "In Progress"
        }
        let httpHeaders = {
            method: "PATCH",
            body: JSON.stringify(body)
        }
        await fetch(`${BASE_URL}${taskId}`, httpHeaders);
        loadBoardHandler();

    }
    async function moveToCodeReviewHandler() {
        let taskId = this.parentElement.id;
        let body = {
            status: "Code Review"
        }
        let httpHeaders = {
            method: "PATCH",
            body: JSON.stringify(body)
        }
        await fetch(`${BASE_URL}${taskId}`, httpHeaders);
        loadBoardHandler();
        
    }
    async function moveToDoneHandler() {
        let taskId = this.parentElement.id;
        let body = {
            status: "Done"
        }
        let httpHeaders = {
            method: "PATCH",
            body: JSON.stringify(body)
        }
        await fetch(`${BASE_URL}${taskId}`, httpHeaders);
        loadBoardHandler();
        
    }
    async function closeHandler() {
        let taskId = this.parentElement.id;
        let httpHeaders = {
            method: "Delete",
        }
        await fetch(`${BASE_URL}${taskId}`, httpHeaders);
        loadBoardHandler();
        
    }


    async function createTaskHandler() {
        let body = {
            title: inputTitle.value,
            description: inputDescription.value,
            status: "ToDo"
        }
        let httpHeaders = {
            method: "POST",
            body: JSON.stringify(body)
        }
        await fetch(BASE_URL, httpHeaders);
        inputTitle.value = "";
        inputDescription.value = "";
        loadBoardHandler();
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

attachEvents();