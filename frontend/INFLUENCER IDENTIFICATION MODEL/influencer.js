document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const resultContainer = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const followers = parseFloat(document.getElementById("followers").value);
        const posts = parseFloat(document.getElementById("posts").value);
        const likes = parseFloat(document.getElementById("likes").value);
        const comments = parseFloat(document.getElementById("comments").value);
        const engagementRate = parseFloat(document.getElementById("engagement-rate").value);

        if (isNaN(followers) || isNaN(posts) || isNaN(likes) || isNaN(comments) || isNaN(engagementRate)) {
            resultContainer.textContent = "Please fill in all fields correctly.";
            return;
        }

        const data = { followers, posts, likes, comments, engagementRate };

        try {
            const response = await fetch("http://127.0.0.1:8000/influencer", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error("Failed to connect to backend");
            }

            const result = await response.json();

            // Store the influencer score in sessionStorage for display in influencer_score.html
            sessionStorage.setItem("influencerScore", result.influencerScore);

            // Redirect to the influencer_score.html page
            window.location.href = "Influencer%20Score/influencer_score.html";
        } catch (error) {
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});