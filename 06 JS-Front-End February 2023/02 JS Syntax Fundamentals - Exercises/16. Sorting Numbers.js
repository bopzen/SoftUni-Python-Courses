function solve(array) {
    let newArray = [];
    array.sort(function(a, b){return a-b});
    while (array.length > 0) {
        newArray.push(array.shift());
        newArray.push(array.pop());
    }
    return newArray;
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));