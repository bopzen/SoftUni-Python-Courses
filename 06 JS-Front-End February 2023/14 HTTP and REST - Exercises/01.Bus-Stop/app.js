function getInfo() {
    let stopID = document.getElementById("stopId").value;
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/businfo/';
    let stopName = document.getElementById("stopName");
    let buses = document.getElementById("buses");
    stopName.textContent = "";
    while (buses.firstElementChild) {
        buses.removeChild(buses.firstElementChild);
    }
    fetch(`${BASE_URL}${stopID}`)
        .then((response) => response.json())
        .then((data) => {
            stopName.textContent = data.name;
            console.log(data.buses)
            busesList = Object.entries(data.buses);
            for (const [busId, minutes] of busesList) {
                let newLi = document.createElement("li");
                newLi.textContent = `Bus ${busId} arrives in ${minutes} minutes`;
                buses.appendChild(newLi);
            }
        })
        .catch((error) => {
            stopName.textContent = "Error"
        });
}