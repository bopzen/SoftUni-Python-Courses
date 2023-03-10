function solve(input) {
    let register = [];
    for (let line of input) {
        let [name, level, items] = line.split(" / ");
        level = Number(level);
        items = items.split(", ");
        register.push({name, level, items})
    }
    sortedRegister = register.sort((h1, h2) => h1.level - h2.level);
    for (const hero of sortedRegister) {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items.join(", ")}`);
    }
}

solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ]
    );

solve([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
    ]    
    );