function solve(input) {
    let n = Number(input.shift());
    let pieces = {};
    for (let i = 0; i < n; i++) {
        let [piece, composer, key] = input.shift().split("|");
        pieces[piece] = {
            "composer": composer, 
            "key": key
        };
    }
    while (true) {
        let command = input.shift();
        if (command === "Stop") {
            break;
        }
        let commandList = command.split("|");
        let action = commandList[0];
        if (action === "Add") {
            let piece = commandList[1];
            let composer = commandList[2];
            let key = commandList[3];
            if (checkIfPieceExists(piece, pieces)) {
                console.log(`${piece} is already in the collection!`);
            } else {
                pieces[piece] = {
                    "composer": composer, 
                    "key": key
                };
                console.log(`${piece} by ${composer} in ${key} added to the collection!`)
            }
        } else if (action === "Remove") {
            let piece = commandList[1];
            if (checkIfPieceExists(piece, pieces)) {
                delete pieces[piece];
                console.log(`Successfully removed ${piece}!`);
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            }
        } else if (action === "ChangeKey") {
            let piece = commandList[1];
            let newKey = commandList[2];
            if (checkIfPieceExists(piece, pieces)) {
                pieces[piece]["key"] = newKey;
                console.log(`Changed the key of ${piece} to ${newKey}!`)
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            }
        }
    }
    for (const piece in pieces) {
        console.log(`${piece} -> Composer: ${pieces[piece]["composer"]}, Key: ${pieces[piece]["key"]}`)
    }

    function checkIfPieceExists(piece, pieces) {
        for (const key in pieces) {
            if (piece === key) {
                return true;
            }
        }
        return false;
    }
}

solve([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',
    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'  
  ]
  )