function solve(array, rotations) {
    for (let index = 0; index < rotations; index++) {
        array.push(array.shift());
        
    }
    console.log(array.join(" "));
}

solve([51, 47, 32, 61, 21], 2);