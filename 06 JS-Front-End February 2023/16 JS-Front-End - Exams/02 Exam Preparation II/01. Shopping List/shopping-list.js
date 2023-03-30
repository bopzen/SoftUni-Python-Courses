function solve(input) {
    let items = input.shift().split("!");
    
    while (true) {
        let command = input.shift();
        if (command === "Go Shopping!") {
            break;
        }
        let commandTokens = command.split(" ");
        let action = commandTokens[0];
        if (action === "Urgent") {
            let item = commandTokens[1];
            if (!items.includes(item)) {
                items.unshift(item);
            }
        } else if (action === "Unnecessary") {
            let item = commandTokens[1];
            if (items.includes(item)) {
                items.splice(items.indexOf(item),1);
            }
        } else if (action === "Correct") {
            let oldItem = commandTokens[1];
            let newItem = commandTokens[2];
            if (items.includes(oldItem)) {
                items[items.indexOf(oldItem)] = newItem;
            }
        } else if (action === "Rearrange") {
            let item = commandTokens[1];
            if (items.includes(item)) {
                items.splice(items.indexOf(item),1)
                items.push(item);
            }
        }
    }
    console.log(items.join(", "));
}

solve((["Tomatoes!Potatoes!Bread",
"Unnecessary Milk",
"Urgent Tomatoes",
"Go Shopping!"])
);

solve((["Milk!Pepper!Salt!Water!Banana",
"Urgent Salt",
"Unnecessary Grapes",
"Correct Pepper Onion",
"Rearrange Grapes",
"Correct Tomatoes Potatoes",
"Go Shopping!"])
);

solve((["Milk!Tomatoes!Pepper!Salt!Water!Banana",
"Urgent Beans",
"Urgent Salt",
"Unnecessary Grapes",
"Correct Pepper Onion",
"Rearrange Tomatoes",
"Correct Tomatoes Potatoes",
"Go Shopping!"])
);