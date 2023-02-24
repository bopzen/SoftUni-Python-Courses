function solve(array, n) {
    let newArray = [];
    for (let index = 0; index < array.length; index += n) {
        newArray.push(array[index])  
    }
    return newArray
}

console.log(solve(['5', 
'20', 
'31', 
'4', 
'20'], 
2
));