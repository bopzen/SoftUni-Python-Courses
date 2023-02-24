function solve(names) {
    names.sort((a, b) => a.localeCompare(b));
    for (let index = 0; index < names.length; index++) {
        console.log(`${index + 1}.${names[index]}`);     
    }
}

solve(["John", "Bob", "Christina", "Ema"]);
solve(["a", "1b", "1a", "b"]);
solve(["a"]);
