function attachGradientEvents() {
    let result = document.getElementById("result");
    let gradient = document.getElementById("gradient-box");
    gradient.addEventListener("mousemove", mouseHandler);
    gradient.addEventListener("mouseout", outHandler);

    function mouseHandler(event) {
        result.textContent = `${Math.trunc(event.offsetX / (event.target.clientWidth - 1) * 100)}%`;
    }   

    function outHandler(event) {
        result.textContent = "";
    }
}