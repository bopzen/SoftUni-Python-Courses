function solve(goldMined) {
    let BTCPrice = 11949.16 / 67.51;
    let dayOfFirstBTC;
    let hasBoughtBTC = false
    let totalGoldMined = 0;
    let totalBTC = 0;
    for (let i = 0; i < goldMined.length; i++) {
        let dailyGoldMined = goldMined[i];
        if ((i+1) % 3 == 0) {
            dailyGoldMined -= dailyGoldMined * 0.3;
        }
        totalGoldMined += dailyGoldMined;
        if (totalGoldMined >= BTCPrice && hasBoughtBTC == false) {
            hasBoughtBTC = true;
            dayOfFirstBTC = i + 1;
        }       
    }
    totalBTC = Math.floor(totalGoldMined / BTCPrice);
    let moneyLeft = (totalGoldMined - totalBTC * BTCPrice) * 67.51 ;
    console.log(`Bought bitcoins: ${totalBTC}`);
    if (totalBTC > 0) {
        console.log(`Day of the first purchased bitcoin: ${dayOfFirstBTC}`)
    }
    console.log(`Left money: ${moneyLeft.toFixed(2)} lv.`);
}

solve([100, 200, 300]);
solve([50, 100]);
solve([3124.15, 504.212, 2511.124]);