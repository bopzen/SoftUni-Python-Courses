function solve() {
    let info = document.getElementsByClassName("info")[0];
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/schedule/';
    let stopID = "depot";
    let departBtn = document.getElementById("depart");
    let arriveBtn = document.getElementById("arrive");
    function depart() {
        fetch(`${BASE_URL}${stopID}`)
            .then((response) => response.json())
            .then((data) => {
                info.textContent = `Next stop ${data.name}`
                departBtn.disabled = true;
                arriveBtn.disabled = false;
            })
            .catch((error) => {
                info.textContent = "Error";
            });
    }

    async function arrive() {
        try {
            const response = await fetch(`${BASE_URL}${stopID}`);
            const data = await response.json();
            info.textContent = `Arriving at ${data.name}`;
            departBtn.disabled = false;
            arriveBtn.disabled = true;
            stopID = data.next;
        }
        catch (error) {
            info.textContent = "Error";
        }
    }

    return {
        depart,
        arrive
    };
}

let result = solve();