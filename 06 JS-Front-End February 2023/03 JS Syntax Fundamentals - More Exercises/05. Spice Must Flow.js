function solve(yield) {
    let totalAmount = 0;
    let days = 0;
    while (yield >= 100) {
        days++;
        totalAmount += yield;
        totalAmount -= 26;
        yield -= 10;
    }
    if (totalAmount >= 26) {
        totalAmount -= 26;
    } else {
        totalAmount = 0;
    }
    console.log(days);
    console.log(totalAmount);
}

solve(111);
solve(450);