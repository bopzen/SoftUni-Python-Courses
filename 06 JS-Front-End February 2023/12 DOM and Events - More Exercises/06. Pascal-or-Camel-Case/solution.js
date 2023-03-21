function solve() {
  let text = document.getElementById("text").value.toLowerCase();
  let convention = document.getElementById("naming-convention").value;
  let result = document.getElementById("result");
  let textArray = text.split(" ");
  let resultText = ""
  if (convention === "Camel Case") {
    resultText += textArray[0];
    for (let i = 1; i < textArray.length; i++) {
      let word = textArray[i];
      resultText += word.charAt(0).toUpperCase() + word.slice(1);  
    }
  } else if (convention === "Pascal Case") {
    for (let i = 0; i < textArray.length; i++) {
      let word = textArray[i];
      resultText += word.charAt(0).toUpperCase() + word.slice(1);  
    }
  } else {
    resultText = "Error!"
  }
  result.textContent = resultText;
}