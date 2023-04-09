window.addEventListener('load', solve);

function solve() {
    let taskCounter = 0;
    const formInputs = {
        title: document.getElementById("title"),
        description: document.getElementById("description"),
        label: document.getElementById("label"),
        points: document.getElementById("points"),
        assignee: document.getElementById("assignee")
    }
    const tasks = [];

    const inputTask = document.getElementById("task-id")

    const createTaskBtn = document.getElementById("create-task-btn");
    createTaskBtn.addEventListener("click", createTaskHandler);
    const deleteTaskBtn = document.getElementById("delete-task-btn");
    deleteTaskBtn.addEventListener("click", deleteTaskHandler);

    const tasksSection = document.getElementById("tasks-section");
    const totalSprintPoints = document.getElementById("total-sprint-points");
    let totalPoints = 0;

    function createTaskHandler() {
        for (const input in formInputs) {
            if (formInputs[input].value == "") {
              return;
            }
        }
        taskCounter++;
        let taskId = `task-${taskCounter}`;
        const {title, description, label, points, assignee} = formInputs;
        let article = createDOMElement("article", tasksSection, null, ["task-card"], taskId);
        let divLabel = createDOMElement("div", article, label.value, ["task-card-label"]);
        if (label.value === "Feature") {
            divLabel.textContent += " " +"⊡";
            divLabel.classList.add("feature");
        } else if (label.value === "Low Priority Bug") {
            divLabel.textContent += " " + "☉";
            divLabel.classList.add("low-priority");
        } else if (label.value === "High Priority Bug") {
            divLabel.textContent += " " + "⚠";
            divLabel.classList.add("high-priority");
        }
        createDOMElement("h3", article, title.value, ["task-card-title"]);
        createDOMElement("p", article, description.value, ["task-card-description"]);
        createDOMElement("div", article, `Estimated at ${points.value} pts`, ["task-card-points"]);
        createDOMElement("div", article, `Assigned to: ${assignee.value}`, ["task-card-assignee"]);
        let divActions = createDOMElement("div", article, null, ["task-card-actions"]);
        let deleteBtn = createDOMElement("button", divActions, "Delete");
        deleteBtn.addEventListener("click", deleteHandler);
        totalPoints += Number(points.value);
        totalSprintPoints.textContent = `Total Points ${totalPoints}pts`;
        let task = {}
        task["id"] = taskId;
        for (const input in formInputs) {   
            task[input] = formInputs[input].value;        
            formInputs[input].value = ""
        }
        tasks.push(task)
    }

    function deleteTaskHandler() {
        document.getElementById(inputTask.value).remove();
        totalPoints -= Number(formInputs.points.value);
        totalSprintPoints.textContent = `Total Points ${totalPoints}pts`;
        for (const input in formInputs) {         
            formInputs[input].value = "";
            formInputs[input].removeAttribute("disabled");
        }
        inputTask.removeAttribute("value");
        createTaskBtn.removeAttribute("disabled");
        deleteTaskBtn.setAttribute("disabled", true);
    }

    function deleteHandler() {
        let taskArticle = this.parentElement.parentElement;
        let currentTaskId = taskArticle.id;
        for (const task of tasks) {
            if (task.id === currentTaskId) {
                formInputs.title.value = task.title;
                formInputs.title.setAttribute("disabled", true);
                formInputs.description.value = task.description;
                formInputs.description.setAttribute("disabled", true);
                formInputs.label.value = task.label;
                formInputs.label.setAttribute("disabled", true);
                formInputs.points.value = task.points;
                formInputs.points.setAttribute("disabled", true);
                formInputs.assignee.value = task.assignee;
                formInputs.assignee.setAttribute("disabled", true);
            }
        }
        inputTask.value = currentTaskId;
        deleteTaskBtn.removeAttribute("disabled");
        createTaskBtn.setAttribute("disabled", true);
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