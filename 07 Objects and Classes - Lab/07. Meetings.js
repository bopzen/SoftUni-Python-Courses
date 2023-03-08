function solve(input) {
    let schedule = {};

    for (const line of input) {
        let [weekday, name] = line.split(" ");
        if (schedule.hasOwnProperty(weekday)) {
            console.log(`Conflict on ${weekday}!`);
        } else {
            schedule[weekday] = name;
            console.log(`Scheduled for ${weekday}`);
        }
    }
    
    for (const key in schedule) {
        console.log(`${key} -> ${schedule[key]}`);
    }
}

solve(['Monday Peter',
'Wednesday Bill',
'Monday Tim',
'Friday Tim']
);