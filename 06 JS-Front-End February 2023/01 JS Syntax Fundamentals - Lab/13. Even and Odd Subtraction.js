function solve(array) {
    let sumEven = 0;
    let sumOdd = 0;
    for (let element of array) {
        if (element % 2 == 0) {
            sumEven += element;
        } else {
            sumOdd += element;
        }
    }
    console.log(sumEven - sumOdd);
}

solve([1,2,3,4,5,6]);