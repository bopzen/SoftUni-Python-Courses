function solve(speed, area) {
    let status;
    let isSpeeding = false;
    let areas = {
        "motorway": 130, 
        "interstate": 90, 
        "city": 50, 
        "residential": 20
    }
    if (speed > areas[area]) {
        isSpeeding = true;
        if (speed - areas[area] <= 20) {
            status = "speeding";
        } else if (speed - areas[area] <= 40) {
            status = "excessive speeding";
        } else {
            status = "reckless driving";
        }
    }
    if (isSpeeding) {
        console.log(`The speed is ${speed - areas[area]} km/h faster than the allowed speed of ${areas[area]} - ${status}`);
    } else {
        console.log(`Driving ${speed} km/h in a ${areas[area]} zone`)
    }
}

solve(40, "city");
solve(21, 'residential');
solve(120, 'interstate');