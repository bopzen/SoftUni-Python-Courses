function solve(number) {
    let digitCheck = number % 10;
    let sumDigits = 0;
    isSame = true;
    while (number > 0) {
        let digit = number % 10;
        if (digit != digitCheck) {
            isSame = false;
        }
        sumDigits += digit;
        number = Math.floor(number / 10);
    }
    console.log(isSame);
    console.log(sumDigits);
}

solve(2222222);