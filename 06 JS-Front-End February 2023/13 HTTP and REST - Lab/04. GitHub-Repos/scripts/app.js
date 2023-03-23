function loadRepos() {
   let result = document.getElementById("res");
   fetch('https://api.github.com/users/testnako11v/repos')
      .then((response) => response.text())
      .then((data) => result.textContent = data)
      .catch((error) => console.log(error));
}