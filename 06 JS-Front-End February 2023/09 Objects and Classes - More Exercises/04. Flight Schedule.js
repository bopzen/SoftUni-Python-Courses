function solve(input) {
    let flightSchedule = [];
    let flights = input[0];
    let statusChanges = input[1];
    let command = input[2][0];
    for (const flight of flights) {
        let [flightNumber, destination] = flight.split(" ");
        flightSchedule.push({
            flightNumber,
            destination,
            status: "none"
        });
    }
    for (const newStatus of statusChanges) {
        let [flightNumber, status] = newStatus.split(" ");
        for (const flight of flightSchedule) {
            if (flight.flightNumber === flightNumber) {
                flight.status = status;
            }
        }
    }
    if (command === "Ready to fly") {
        for (const flight of flightSchedule) {
            if (flight.status === "none") {
                flight.status = command;
                console.log(`{ Destination: '${flight.destination}', Status: '${flight.status}' }`)
            }
        }
    } else {
        let filteredFlights = flightSchedule.filter((f) => f.status === command);
        for (const flight of filteredFlights) {
            console.log(`{ Destination: '${flight.destination}', Status: '${flight.status}' }`)
        }
    }
}

solve([['WN269 Delaware',
'FL2269 Oregon',
 'WN498 Las Vegas',
 'WN3145 Ohio',
 'WN612 Alabama',
 'WN4010 New York',
 'WN1173 California',
 'DL2120 Texas',
 'KL5744 Illinois',
 'WN678 Pennsylvania'],
 ['DL2120 Cancelled',
 'WN612 Cancelled',
 'WN1173 Cancelled',
 'SK430 Cancelled'],
 ['Cancelled']
]
);
solve([['WN269 Delaware',
'FL2269 Oregon',
 'WN498 Las Vegas',
 'WN3145 Ohio',
 'WN612 Alabama',
 'WN4010 New York',
 'WN1173 California',
 'DL2120 Texas',
 'KL5744 Illinois',
 'WN678 Pennsylvania'],
 ['DL2120 Cancelled',
 'WN612 Cancelled',
 'WN1173 Cancelled',
 'SK330 Cancelled'],
 ['Ready to fly']
]
);