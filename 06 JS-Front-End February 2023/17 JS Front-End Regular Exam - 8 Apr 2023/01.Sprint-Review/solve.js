function solve(input) {
    let n = input.shift();
    let assignees = {};
    for (let i = 0; i < n; i++) {
        let [assignee, taskId, title, status, points] = input.shift().split(":");
        if (!checkIfAssigneeExists(assignee, assignees)) {
            assignees[assignee] = [];
        }
        let task = {taskId, title, status, points: Number(points)};
        assignees[assignee].push(task);
    }
    while(input.length > 0) {
        let commandInputs = input.shift().split(":");
        let command = commandInputs.shift();
        if (command === "Add New") {
            let [assignee, taskId, title, status, points] = commandInputs;
            if (!checkIfAssigneeExists(assignee, assignees)) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
            } else {
                let task = {taskId, title, status, points: Number(points)};
                assignees[assignee].push(task);
            }
        } else if (command === "Change Status") {
            let [assignee, taskId, newStatus] = commandInputs;
            if (!checkIfAssigneeExists(assignee, assignees)) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
            } else {
                let taskExists = false;
                for (const task of assignees[assignee]) {
                    if (task.taskId === taskId) {
                        task.status = newStatus;
                        taskExists = true;
                        break;
                        }
                }
                if (!taskExists) {
                    console.log(`Task with ID ${taskId} does not exist for ${assignee}!`)
                }
            }
        } else if (command === "Remove Task") {
            let [assignee, index] = commandInputs;
            index = Number(index);
            if (!checkIfAssigneeExists(assignee, assignees)) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
            } else {
                if (index < 0 || index >= assignees[assignee].length) {
                    console.log("Index is out of range!");
                } else {
                    assignees[assignee].splice(index, 1);
                }
            }
        }
    }
    let totalPoints = {
        "ToDo": 0,
        "In Progress": 0,
        "Code Review": 0,
        "Done": 0
    }
    for (const tasks of Object.values(assignees)) {
        for (const task of tasks) {
            totalPoints[task.status] += task.points
        }
    }
    for (const key in totalPoints) {
        if (key === "Done") {
            console.log(`Done Points: ${totalPoints[key]}pts`);
        } else {
            console.log(`${key}: ${totalPoints[key]}pts`);
        }
    }
    if (Number(totalPoints["Done"]) >= Number(totalPoints["ToDo"]) + Number(totalPoints["In Progress"]) + Number(totalPoints["Code Review"])) {
        console.log("Sprint was successful!")
    } else {
        console.log("Sprint was unsuccessful...")
    }


    function checkIfAssigneeExists(assignee, assignees) {
        for (const key in assignees) {
            if (assignee === key) {
                return true;
            }
        }
        return false;
    }
}

solve([
    '5',
    'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
    'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
    'Peter:BOP-1211:POC:Code Review:5',
    'Georgi:BOP-1212:Investigation Task:Done:2',
    'Mariya:BOP-1213:New Account Page:In Progress:13',
    'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
    'Change Status:Peter:BOP-1290:ToDo',
    'Remove Task:Mariya:1',
    'Remove Task:Joro:1',
]
);

solve([
    '4',
    'Kiril:BOP-1213:Fix Typo:Done:1',
    'Peter:BOP-1214:New Products Page:In Progress:2',
    'Mariya:BOP-1215:Setup Routing:ToDo:8',
    'Georgi:BOP-1216:Add Business Card:Code Review:3',
    'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
    'Change Status:Georgi:BOP-1216:Done',
    'Change Status:Will:BOP-1212:In Progress',
    'Remove Task:Georgi:3',
    'Change Status:Mariya:BOP-1215:Done',
]
);