function solve(jsonText) {
    let jsonObject = JSON.parse(jsonText);
    
    let entries = Object.entries(jsonObject)
    for (const [ key, value ] of entries) {
        console.log(`${key}: ${value}`)
    }
}

solve('{"name": "George", "age": 40, "town": "Sofia"}');