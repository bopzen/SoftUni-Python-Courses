function attachEventsListeners() {
    let inputDistance = document.getElementById("inputDistance");
    let outputDistance = document.getElementById("outputDistance");
    let selectInput = document.getElementById("inputUnits");
    let selectOutput = document.getElementById("outputUnits");
    let conversionRates = {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.34,
        "yrd": 0.9144,
        "ft": 0.3048,
        "in": 0.0254
    }
    let button = document.getElementById("convert");
    button.addEventListener("click", clickHandler);

    function clickHandler() {
        outputDistance.value = Number(inputDistance.value) * conversionRates[selectInput.value] / conversionRates[selectOutput.value];
    }
}