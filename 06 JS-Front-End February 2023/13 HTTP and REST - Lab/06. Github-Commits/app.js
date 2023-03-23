function loadCommits() {
    let username = document.getElementById("username").value;
    let repo = document.getElementById("repo").value;
    let commits = document.getElementById("commits");

    while (commits.firstElementChild) {
        commits.removeChild(commits.firstElementChild);
    }
    fetch(`https://api.github.com/repos/${username}/${repo}/commits`)
        .then((response) => {
            if (response.ok == false) {
                throw new Error(`Error: ${response.status} ${response.statusText}`)
            }
            return response.json()})
        .then((data) => {
            for (const commit of data) {
                let author = commit.commit.author.name;
                let message = commit.commit.message;
                let newLi = document.createElement("li");
                newLi.textContent = `${author}: ${message}`;
                commits.appendChild(newLi);
            }
        })
        .catch((error) => {
            let newLi = document.createElement("li");
                newLi.textContent = `${error.message}`;
                commits.appendChild(newLi);
        });
}