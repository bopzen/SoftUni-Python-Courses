function solve() {
  let rightAnswers = ["onclick", "JSON.stringify()", "A programming API for HTML and XML documents"]
  let sections = Array.from(document.getElementsByTagName("section"));
  let answers = Array.from(document.querySelectorAll(".answer-text"));
  let result = document.querySelector("#results > li > h1");
  let guessed = 0;
  let i = 0;

  for (const answer of answers) {
    answer.addEventListener("click", clickHandler);
  }

  function clickHandler(event) {
    let currentAnswer = event.currentTarget.textContent;
    if (rightAnswers.includes(currentAnswer)) {
      guessed++;
    }
    if (i < 2) {
      sections[i].style.display = "none";
      sections[i+1].style.display = "block";   
    }
    if (i === 2) {
      sections[i].style.display = "none";
      if (guessed === 3) {
        result.textContent = "You are recognized as top JavaScript fan!";
      } else {
        result.textContent = `You have ${guessed} right answers`;
      }
        document.getElementById("results").style.display = "block"; 
    }
    i++;
  }  
}
