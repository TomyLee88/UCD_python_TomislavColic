document.addEventListener('DOMContentLoaded', function() {
    const postWrappers = document.querySelectorAll('.blog_wrapper');
    postWrappers.forEach(function(postWrapper) {
        postWrapper.addEventListener('click', function() {
            const postContent = postWrapper.querySelector('.card-text');
            if (postContent) {
                postContent.classList.toggle('hidden');
            }
        });
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const likeButtons = document.querySelectorAll(".upvote-button");
    likeButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const postId = button.getAttribute("data-post-id");
            const likeCountElement = document.querySelector(`.like-count[data-post-id="${postId}"]`);
            const currentLikes = parseInt(likeCountElement.textContent);
            const newLikes = currentLikes + 1;
            likeCountElement.textContent = `${newLikes} Likes`;
        });
    });
});

