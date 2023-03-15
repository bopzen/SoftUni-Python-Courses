function solve(input) {
    let leaders = [];
    for (const line of input) {
        if (line.includes("arrives")) {
            let newLeaderName = line.replace(" arrives", "");
            let leaderObj = {
                "name": newLeaderName,
                "count": 0,
                "army": []
            }
            leaders.push(leaderObj)
        } else if (line.includes("defeated")) {
            let currentLeader = line.replace(" defeated", "");
            let index;
            for (i = 0; i < leaders.length; i++) {
                if (leaders[i]["name"] === currentLeader) {
                    index = i;
                    break;
                }
            }
            leaders.splice(index, 1);
        } else if (line.includes(" + ")) {
            let [armyName, armyCount] = line.split(" + ");
            armyCount = Number(armyCount);
            for (let leader of leaders) {
                let armies = leader["army"];
                for (const army of armies) {
                    if (army["name"] === armyName) {
                        army["count"] += armyCount;
                        leader["count"] += armyCount;
                        break;
                    }
                }
            }
        } else {
            let [leaderName, army] = line.split(": ");
            let [armyName, armyCount] = army.split(", ");
            armyCount = Number(armyCount);
            let newArmy = {"name": armyName, "count": armyCount};
            for (const leader of leaders) {
                if (leader["name"] === leaderName) {
                    leader["army"].push(newArmy);
                    leader["count"] += armyCount;
                    break;
                }                 
            }
        }
    }
    for (const leader of leaders.sort((a, b) => b.count - a.count)) {
        console.log(`${leader["name"]}: ${leader["count"]}`);
        for (const army of leader["army"].sort((a, b) => b.count - a.count)) {
            console.log(`>>> ${army["name"]} - ${army["count"]}`)
        }
    }
}

solve(['Rick Burr arrives', 'Fergus: Wexamp, 30245', 'Rick Burr: Juard, 50000', 'Findlay arrives', 'Findlay: Britox, 34540', 'Wexamp + 6000', 'Juard + 1350', 'Britox + 4500', 'Porter arrives', 'Porter: Legion, 55000', 'Legion + 302', 'Rick Burr defeated', 'Porter: Retix, 3205']);

solve(['Rick Burr arrives', 'Findlay arrives', 'Rick Burr: Juard, 1500', 'Wexamp arrives', 'Findlay: Wexamp, 34540', 'Wexamp + 340', 'Wexamp: Britox, 1155', 'Wexamp: Juard, 43423']);