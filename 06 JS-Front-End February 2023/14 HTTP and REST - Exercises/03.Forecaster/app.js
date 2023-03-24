function attachEvents() {
    let location = document.getElementById("location");
    let button = document.getElementById("submit");
    let forecast = document.getElementById("forecast");
    let current = document.getElementById("current");
    let upcoming = document.getElementById("upcoming");
    button.addEventListener("click", clickHandler);
    let conditionsDict = {
        "Sunny": "&#x2600",
        "Partly sunny": "&#x26C5",
        "Overcast": "&#x2601",
        "Rain": "&#x2614",
        "Degrees": "&#176"
    }

    let code;
    async function clickHandler() {
        try {
            let locationInput = location.value;
            let response = await fetch('http://localhost:3030/jsonstore/forecaster/locations');
            let data = await response.json();
            let searchedLocation = data.find((l) => l.name === locationInput);
            code = searchedLocation.code;

            response = await fetch(`http://localhost:3030/jsonstore/forecaster/today/${code}`);
            data = await response.json();
            console.log(data)
            showCurrent(data);

            response = await fetch(`http://localhost:3030/jsonstore/forecaster/upcoming/${code}`);
            data = await response.json();
            showUpcoming(data);
            console.log(data)

        }
        catch (error) {
            forecast.style.display = "";
            let clearCurrent = document.querySelector(".forecasts");
            if (clearCurrent) {
                clearCurrent.remove();
            }
            let clearUpcoming = document.querySelector(".forecast-info");
            if (clearUpcoming) {
                clearUpcoming.remove();
            }
            let currentForecasts = document.createElement("div");
            currentForecasts.classList.add("forecasts");
            currentForecasts.textContent = "Error";
            current.appendChild(currentForecasts);
        }
    }

    function showCurrent(data) {
        forecast.style.display = "";
        let clearContent = document.querySelector(".forecasts");
        if (clearContent) {
            clearContent.remove();
        }
        let currentForecasts = document.createElement("div");
        currentForecasts.classList.add("forecasts");
        current.appendChild(currentForecasts);

        let spanSymbol = document.createElement("span");
        spanSymbol.classList.add("condition","symbol");
        spanSymbol.innerHTML = conditionsDict[data.forecast.condition];       
        currentForecasts.appendChild(spanSymbol);

        let spanCondition = document.createElement("span");
        spanCondition.classList.add("condition");
        currentForecasts.appendChild(spanCondition);

        let spanLocation = document.createElement("span");
        spanLocation.classList.add("forecast-data");
        spanLocation.textContent = data.name;
        spanCondition.appendChild(spanLocation);

        let spanTemperature = document.createElement("span");
        spanTemperature.classList.add("forecast-data");
        spanTemperature.innerHTML = `${data.forecast.low}${conditionsDict["Degrees"]}/${data.forecast.high}${conditionsDict["Degrees"]}`;
        spanCondition.appendChild(spanTemperature);

        let spanInfo = document.createElement("span");
        spanInfo.classList.add("forecast-data");
        spanInfo.textContent = `${data.forecast.condition}`;
        spanCondition.appendChild(spanInfo);
    }

    function showUpcoming(data) {
        let clearContent = document.querySelector(".forecast-info");
        if (clearContent) {
            clearContent.remove();
        }

        let upcomingForecasts = document.createElement("div");
        upcomingForecasts.classList.add("forecast-info");
        upcoming.appendChild(upcomingForecasts);
        for (const {condition, high, low} of data.forecast) {
            let spanUpcoming = document.createElement("span");
            spanUpcoming.classList.add("upcoming");
            upcomingForecasts.appendChild(spanUpcoming);

            let spanSymbol = document.createElement("span");
            spanSymbol.classList.add("symbol");
            spanSymbol.innerHTML = `${conditionsDict[condition]}`;
            spanUpcoming.appendChild(spanSymbol);

            let spanTemperature = document.createElement("span");
            spanTemperature.classList.add("forecast-data");
            spanTemperature.innerHTML = `${low}${conditionsDict["Degrees"]}/${high}${conditionsDict["Degrees"]}`;
            spanUpcoming.appendChild(spanTemperature);

            let spanInfo = document.createElement("span");
            spanInfo.classList.add("forecast-data");
            spanInfo.textContent = `${condition}`;
            spanUpcoming.appendChild(spanInfo);
        }
    }
}

attachEvents();