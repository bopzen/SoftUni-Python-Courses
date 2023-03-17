function solve() {
  let textArea = document.getElementById("input");
  let sentences = textArea.value.split(".");
  sentences.pop();
  let output = document.getElementById("output");
  while (sentences.length > 0) {
    let paragraphArr = sentences.splice(0, 3).map((s) => s.trimStart());
    let paragraph = document.createElement("p");
    paragraph.textContent = paragraphArr.join(".") + ".";
    output.appendChild(paragraph);
  }
}
