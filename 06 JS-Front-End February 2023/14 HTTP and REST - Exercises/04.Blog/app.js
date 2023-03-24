function attachEvents() {
    let loadPostsBtn = document.getElementById("btnLoadPosts");
    let viewPostBtn = document.getElementById("btnViewPost");
    let postsOptions = document.getElementById("posts");
    let postTitle = document.getElementById("post-title");
    let postBody = document.getElementById("post-body");
    let postComments = document.getElementById("post-comments");

    loadPostsBtn.addEventListener("click", clickLoadHandler);
    viewPostBtn.addEventListener("click", clickViewHandler);

    let posts = [];
    async function clickLoadHandler() {
        try {
            const response = await fetch("http://localhost:3030/jsonstore/blog/posts");
            const data = await response.json();
            posts = Object.values(data);
            for (const {body, id, title} of posts) {
                let option = document.createElement("option");
                option.value = id;
                option.textContent = title;
                postsOptions.appendChild(option);
            }
        }
        catch (error) {
            console.log(error)
        }
    }

    async function clickViewHandler() {
        try {
            postComments.innerHTML = "";
            let selectedPost = postsOptions.value;
            let currentPost = posts.find((p) => p.id === selectedPost);
            postTitle.textContent = currentPost.title;
            postBody.textContent = currentPost.body;
            
            const response = await fetch("http://localhost:3030/jsonstore/blog/comments");
            const data = await response.json();      
            let comments = Object.values(data);
            for (const {id, postId, text} of comments) {
                if (postId === selectedPost) {
                    let newComment = document.createElement("li");
                    newComment.id = id;
                    newComment.textContent = text;
                    postComments.appendChild(newComment);
                }
            }
        }
        catch (error) {
            console.log(error)
        }
    }
}

attachEvents();