function solve(input) {
    let targetTickness = input.shift();
    for (const chunk  of input) {
        process(chunk);
    }

    function process(chunk) {
        let cut = (x) => x / 4;
        let lap = (x) => x - x * 0.2;
        let grind = (x) => x - 20;
        let etch = (x) => x - 2;
        let xRay = (x) => x + 1;
        let transtportingAndWashing = (x) => Math.floor(x);

        let operations = {
            "cut": 0,
            "lap": 0,
            "grind": 0,
            "etch": 0
        }
        console.log(`Processing chunk ${chunk} microns`)
        while (chunk != targetTickness) {
            while (cut(chunk) >= targetTickness) {
                chunk = cut(chunk);
                operations["cut"]++;
            }            
            if (operations["cut"] > 0) {
                console.log(`Cut x${operations["cut"]}`);
                chunk = transtportingAndWashing(chunk);
                console.log("Transporting and washing");
            }

            while (lap(chunk) >= targetTickness) {
                chunk = lap(chunk);
                operations["lap"]++;
            }
            if (operations["lap"] > 0) {
                console.log(`Lap x${operations["lap"]}`);
                chunk = transtportingAndWashing(chunk);
                console.log("Transporting and washing");
            }          

            while (grind(chunk) >= targetTickness) {
                chunk = grind(chunk);
                operations["grind"]++;
            }
            if (operations["grind"] > 0) {
                console.log(`Grind x${operations["grind"]}`);
                chunk = transtportingAndWashing(chunk);
                console.log("Transporting and washing");
            }

            while (etch(chunk) >= targetTickness - 1) {
                chunk = etch(chunk);
                operations["etch"]++;
            }
            if (operations["etch"] > 0) {
                console.log(`Etch x${operations["etch"]}`);
                chunk = transtportingAndWashing(chunk);
                console.log("Transporting and washing");
            }            

            if (chunk < targetTickness) {
                chunk = xRay(chunk);
                console.log(`X-ray x1`)
            }     
        }
        console.log(`Finished crystal ${chunk} microns`)      
    }
}

solve([1375, 50000]);
solve([1000, 4000, 8100]);