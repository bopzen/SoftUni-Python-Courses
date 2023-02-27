function solve(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let brokenHelmets = Math.floor(lostFights / 2);
    let brokenSwords = Math.floor(lostFights / 3);
    let brokenShields = Math.floor(lostFights / 6);
    let brokenArmors = Math.floor(lostFights / 12);
    let expenses = brokenHelmets * helmetPrice + brokenSwords * swordPrice + brokenShields * shieldPrice + brokenArmors * armorPrice;
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}

solve(7,
    2,
    3,
    4,
    5
    );