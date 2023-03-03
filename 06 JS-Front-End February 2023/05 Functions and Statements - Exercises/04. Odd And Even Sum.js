function printOddEvenSums(number) {
    let numbers = number.toString().split("").map(Number);
    let sumEven = sum(numbers.filter((x) => x % 2 === 0));
    let sumOdd = sum(numbers.filter((x) => x % 2 != 0));
    return `Odd sum = ${sumOdd}, Even sum = ${sumEven}`;

    function sum(array) {
        let sum = 0;
        for (const element of array) {
            sum += element;
        }
        return sum;
    }
}

console.log(printOddEvenSums(1000435));