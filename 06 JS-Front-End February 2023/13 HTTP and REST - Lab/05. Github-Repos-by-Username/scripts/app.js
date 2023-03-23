function loadRepos() {
	let repos = document.getElementById("repos");
	let username = document.getElementById("username").value;

	while (repos.firstElementChild) {
		repos.removeChild(repos.firstElementChild);
	}

	fetch (`https://api.github.com/users/${username}/repos`)
		.then((response) => response.json())
		.then((data) => showRepos(data))
		.catch((error) => showError(error));


	function showRepos(data) {
		for (const repo of data) {
			let fullName = repo.full_name;
			let url = repo.html_url;
			let newList = document.createElement("li");
			let newAnchor = document.createElement("a");
			newAnchor.setAttribute("href", url);
			newAnchor.textContent = fullName;
			newList.appendChild(newAnchor);
			repos.appendChild(newList);
		}

	}
	function showError(error) {
		let newList = document.createElement("li");
		newList.textContent = error;
		repos.appendChild(newList);
	}
	
}