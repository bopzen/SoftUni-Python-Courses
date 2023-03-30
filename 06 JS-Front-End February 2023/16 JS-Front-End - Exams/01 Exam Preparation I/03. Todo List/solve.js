function attachEvents() {
    const BASE_URL = "http://localhost:3030/jsonstore/tasks/";
    const tasksContainer = document.getElementById("todo-list");
    const title = document.getElementById("title");
    const addBtn = document.getElementById("add-button");
    addBtn.addEventListener("click", addHandler);
    const loadBtn = document.getElementById("load-button");
    loadBtn.addEventListener("click", loadHandler);

    async function loadHandler(e) {
        if (e) {
            e.preventDefault();
        }
        tasksContainer.innerHTML = "";
        try {
            let response = await fetch(BASE_URL);
            let data = await response.json();         
            let tasks = Object.values(data);
            for (const task of tasks) {
                const li = document.createElement("li");
                const span = document.createElement("span");
                const removeBtn = document.createElement("button");
                const editBtn = document.createElement("button");

                li.id = task._id;               
                span.textContent = task.name;               
                removeBtn.textContent = "Remove";         
                editBtn.textContent = "Edit";

                removeBtn.addEventListener("click", removeHandler);   
                editBtn.addEventListener("click", editHandler);

                li.appendChild(span);
                li.appendChild(removeBtn);
                li.appendChild(editBtn);
                tasksContainer.appendChild(li);
            }
        }
        catch (error) {
            console.log(error);
        }    
    }

    async function addHandler(e) {
        if (e) {
            e.preventDefault();
        }
        const name = title.value
        try {
            let httpHeader = {
                method: "POST",
                body: JSON.stringify({ name })
            }
            await fetch(BASE_URL, httpHeader);
            loadHandler();
        }
        catch (error) {
            console.log(error)
        }
    }

    async function removeHandler(e) {
        if (e) {
            e.preventDefault();
        }
        let taskId = e.currentTarget.parentElement.id;
        try {
            let httpHeader = {
                method: "DELETE"
            }
            await fetch(`${BASE_URL}${taskId}`, httpHeader);
            loadHandler();
        }
        catch (error) {
            console.log(error)
        }
    }

    function editHandler(e) {
        let task = e.currentTarget.parentElement;
        let taskChildren = Array.from(task.children);
        let span = taskChildren[0];
        let editBtn = taskChildren[2];
        let taskName = span.textContent;
        span.remove();
        editBtn.remove()
        let input = document.createElement("input");
        input.value = taskName;
        task.prepend(input);
        let submitBtn = document.createElement("button");
        submitBtn.textContent = "Submit";
        submitBtn.addEventListener("click", submitHandler);
        task.appendChild(submitBtn);
        
    }

    async function submitHandler(e) {
        let task = e.currentTarget.parentElement;
        let taskId = task.id;
        let taskChildren = Array.from(task.children);
        let input = taskChildren[0];
        try {
            let httpHeader = {
                method: "PATCH",
                body: JSON.stringify({ name: input.value })
            }
            await fetch(`${BASE_URL}${taskId}`, httpHeader);
            loadHandler();
        }
        catch (error) {
            console.log(error)
        }
    }  
}

attachEvents();
