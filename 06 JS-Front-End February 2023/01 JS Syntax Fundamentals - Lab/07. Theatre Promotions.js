function solve (typeOfDay, age) {
    let price = 0;
    if (typeOfDay === "Weekday") {
        if (0 <= age && age <= 18) {
            price = 12;
            console.log(`${price}$`);
        } else if (18 < age && age <= 64) {
            price = 18;
            console.log(`${price}$`);
        } else if (64 < age && age <= 122) {
            price = 12;
            console.log(`${price}$`);
        } else {
            console.log("Error!");
        }
    } else if (typeOfDay === "Weekend") {
        if (0 <= age && age <= 18) {
            price = 15;
            console.log(`${price}$`);
        } else if (18 < age && age <= 64) {
            price = 20;
            console.log(`${price}$`);
        } else if (64 < age && age <= 122) {
            price = 15;
            console.log(`${price}$`);
        } else {
            console.log("Error!");
        }
    } else if (typeOfDay === "Holiday") {
        if (0 <= age && age <= 18) {
            price = 5;
            console.log(`${price}$`);
        } else if (18 < age && age <= 64) {
            price = 12;
            console.log(`${price}$`);
        } else if (64 < age && age <= 122) {
            price = 10;     
            console.log(`${price}$`);
        } else {
            console.log("Error!");
        }
    } 
}

solve('Holiday', -12);
