document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const resultContainer = document.createElement("div");
    resultContainer.id = "result";
    form.appendChild(resultContainer);

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
            const response = await fetch("YOUR_BACKEND_URL/influencer", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            resultContainer.textContent = `Influencer Status: ${result.status}`;
        } catch (error) {
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});
