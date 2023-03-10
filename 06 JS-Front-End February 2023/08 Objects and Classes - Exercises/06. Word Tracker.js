function solve(input) {
    let words = input.shift().split(" ");
    let occurances = {};
    for (const word of words) {
        occurances[word] = 0;
    }
    for (const word of input) {
        if (occurances.hasOwnProperty(word)) {
            occurances[word]++;
        }
    }
    let occurancesSorted = Object.entries(occurances);
    occurancesSorted.sort((a, b) => b[1] - a[1]);
    for (const [key, value] of occurancesSorted) {
        console.log(`${key} - ${value}`);
    }
}

solve([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
    );

solve([
    'is the', 
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence']
    );