function solve(input) {
    let usersList = [];
    let articlesList = [];
    let comments = {};
    for (const line of input) {
        if (line.split(" ").length === 2) {
            let [command, item] = line.split(" ");
            if (command === "user") {
                if (!usersList.includes(item)) {
                    usersList.push(item);
                }              
            } else if (command === "article") {
                if (!articlesList.includes(item)) {
                    articlesList.push(item);
                }          
            }
        } else {
            let [username, article, title, content] = line
                .replace("posts on", "|")
                .replace(":", " |")
                .replace(",", " |")
                .split(" | ");
            
            if (usersList.includes(username) && articlesList.includes(article)) {
                if (!comments.hasOwnProperty(article)) {
                    comments[article] = [{[username]: `--- From user ${username}: ${title} - ${content}`}];
                } else {
                    comments[article].push({[username]: `--- From user ${username}: ${title} - ${content}`})
                }
            }
        }
    }
    let sortedArticles = Object.entries(comments).sort((a,b) => b[1].length - a[1].length);
    for (const [article, comments] of sortedArticles) {
        console.log(`Comments on ${article}`);
        let sortedComments = comments.sort((a, b) => Object.keys(a)[0].localeCompare(Object.keys(b)[0]));
        for (const comment of sortedComments) {
            console.log(Object.values(comment)[0]);
        }
    }
}

solve(['user aUser123', 'someUser posts on someArticle: NoTitle, stupidComment', 'article Books', 'article Movies', 'article Shopping', 'user someUser', 'user uSeR4', 'user lastUser', 'uSeR4 posts on Books: I like books, I do really like them', 'uSeR4 posts on Movies: I also like movies, I really do', 'someUser posts on Shopping: title, I go shopping every day', 'someUser posts on Movies: Like, I also like movies very much']);

solve(['user Mark', 'Mark posts on someArticle: NoTitle, stupidComment', 'article Bobby', 'article Steven', 'user Liam', 'user Henry', 'Mark posts on Bobby: Is, I do really like them', 'Mark posts on Steven: title, Run', 'someUser posts on Movies: Like']);
