function solve(input) {
    let uniqueArrays = new Set();
    for (const array of input) {
        let line = JSON.parse(array).sort((a, b) => b - a);
        line = JSON.stringify(line);
        uniqueArrays.add(line);
    }
    let uniqueSorted = Array.from(uniqueArrays).map(JSON.parse).sort((a, b) => a.length - b.length);
    for (const entry of uniqueSorted) {
        console.log(`[${entry.join(", ")}]`);
    }
}


solve(["[-3, -2, -1, 0, 1, 2, 3, 4]",
"[10, 1, -17, 0, 2, 13]",
"[4, -3, 3, -2, 2, -1, 1, 0]"]
);
solve(["[7.14, 7.180, 7.339, 80.099]",
"[7.339, 80.0990, 7.140000, 7.18]",
"[7.339, 7.180, 7.14, 80.099]"]
);
