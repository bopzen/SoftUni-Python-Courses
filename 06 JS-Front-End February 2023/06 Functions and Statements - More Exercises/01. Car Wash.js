function cleanCar(commands) {
    let clean = 0;
    for (const operation of commands) {
        if (operation === "soap") {
            clean += 10;
        } else if (operation === "water") {
            clean += clean * 0.2;
        } else if (operation === "vacuum cleaner") {
            clean += clean * 0.25;
        } else if (operation === "mud") {
            clean -= clean * 0.1;
        }
    }
    console.log(`The car is ${clean.toFixed(2)}% clean.`);
}

cleanCar(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water']);
cleanCar(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]);