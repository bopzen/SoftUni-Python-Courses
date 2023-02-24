function solve(firstNum, secondNum) {
    let sum = 0;
    let array = [];
    for (let i = firstNum; i <= secondNum; i++) {
        array.push(i);
        sum += i;
    }
    console.log(array.join(" "));
    console.log(`Sum: ${sum}`);
}

solve(5, 10);