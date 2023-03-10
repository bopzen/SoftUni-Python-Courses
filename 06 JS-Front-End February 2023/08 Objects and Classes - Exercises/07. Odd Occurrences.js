function solve(input) {
    input = input.toLowerCase().split(" ");
    let occurances = {};
    for (const item of input) {
        if (occurances.hasOwnProperty(item)) {
            occurances[item]++;
        } else {
            occurances[item] = 1;
        }
    }
    let ocurrancesArr = Object.entries(occurances);
    let result = [];
    for (const [key, value] of ocurrancesArr) {
        if (value % 2 != 0) {
            result.push(key);
        }
    }
    console.log(result.join(" "));
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
solve('Cake IS SWEET is Soft CAKE sweet Food');