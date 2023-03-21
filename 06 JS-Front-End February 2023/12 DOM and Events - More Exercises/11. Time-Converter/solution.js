function attachEventsListeners() {
    let buttons = Array.from(document.querySelectorAll("div input:last-child"));
    for (const button of buttons) {
        button.addEventListener("click", clickHandler);
    }

    function clickHandler(event) {
        let element = event.currentTarget;
        let timeframe = element.parentElement.children[0].textContent
        console.log(timeframe)
        let days = document.getElementById("days");
        let hours = document.getElementById("hours");
        let minutes = document.getElementById("minutes");
        let seconds = document.getElementById("seconds");
        switch (timeframe) {
            case "Days: ":
                hours.value = Number(days.value) * 24;
                minutes.value = hours.value * 60;
                seconds.value = minutes.value * 60;
            case "Hours: ":
                days.value = Number(hours.value) / 24;
                minutes.value = Number(hours.value) * 60;
                seconds.value = minutes.value * 60;
            case "Minutes: ":
                hours.value = Number(minutes.value) / 60;
                days.value = hours.value / 24;
                seconds.value = Number(minutes.value) * 60;
            case "Seconds: ":
                minutes.value = Number(seconds.value) / 60;
                hours.value = minutes.value / 60;
                days.value = hours.value / 24;
        }
    } 
}