function modifyNumber(number) {
    while (getAverage(number) < 5) {
        number = Number(number.toString() + "9");
    }
    return number;

    function getAverage(number) {
        let digits = number.toString().split("").map(Number);
        let sumDigits = 0;
        for (const digit of digits) {
            sumDigits += digit;
        }
        return sumDigits / digits.length;
    }
}

console.log(modifyNumber(101));
console.log(modifyNumber(5835));