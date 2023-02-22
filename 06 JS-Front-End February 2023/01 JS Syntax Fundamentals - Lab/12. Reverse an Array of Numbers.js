function solve(n, array) {
    let newArray = [];
    for (let index = 0; index < n; index++) {
        newArray.unshift(array[index]); 
    }
    console.log(newArray.join(" "));
}

solve(3, [10, 20, 30, 40, 50]);