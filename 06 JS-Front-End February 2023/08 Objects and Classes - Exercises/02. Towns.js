function solve(input) {
    let towns = [];
    for (const line of input) {
        let [town, latitude, longitude] = line.split(" | ");
        latitude = Number(latitude).toFixed(2);
        longitude = Number(longitude).toFixed(2);
        let townObject = {
            town, 
            latitude,
            longitude
        }
        towns.push(townObject)
    }
    for (const town of towns) {
        console.log(town);
    }
}

solve(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']
);

solve(['Plovdiv | 136.45 | 812.575']
);