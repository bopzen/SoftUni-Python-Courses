function solve(groupSize, groupType, weekday) {
    let totalPrice = 0;
    let pricePerNight;
    if (groupType === "Students") {
        if (weekday === "Friday") {
            pricePerNight = 8.45;
        } else if (weekday === "Saturday") {
            pricePerNight = 9.80;
        } else if (weekday === "Sunday") {
            pricePerNight = 10.46;
        }
        totalPrice = groupSize * pricePerNight;
        if (groupSize >= 30) {
            totalPrice -= totalPrice * 0.15;
        }
    } else if (groupType === "Business") {
        if (weekday === "Friday") {
            pricePerNight = 10.90;
        } else if (weekday === "Saturday") {
            pricePerNight = 15.60;
        } else if (weekday === "Sunday") {
            pricePerNight = 16;
        }
        totalPrice = groupSize * pricePerNight;
        if (groupSize >= 100) {
            totalPrice -= 10 * pricePerNight;
        }
    } else if (groupType === "Regular") {
        if (weekday === "Friday") {
            pricePerNight = 15;
        } else if (weekday === "Saturday") {
            pricePerNight = 20;
        } else if (weekday === "Sunday") {
            pricePerNight = 22.50;
        }
        totalPrice = groupSize * pricePerNight;
        if (10 <= groupSize && groupSize <= 20) {
            totalPrice -= totalPrice * 0.05;
        }
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}

solve(30,
    "Students",
    "Sunday"
    );

solve(40,
    "Regular",
    "Saturday"   
    );
