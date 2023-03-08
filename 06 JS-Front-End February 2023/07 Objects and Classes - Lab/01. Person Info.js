function solve(firstName, lastName, age) {
    age = Number(age);
    let person = {
        firstName,
        lastName, 
        age
    }
    return person
}

console.log(solve("Peter", 
"Pan",
"20"
));