// Wait for the DOM content to be fully loaded before executing the script
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const resultContainer = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const likes = parseFloat(document.getElementById("likes").value);
        const shares = parseFloat(document.getElementById("shares").value);
        const comments = parseFloat(document.getElementById("comments").value);
        const engagementRate = parseFloat(document.getElementById("engagement-rate").value);

        if (isNaN(likes) || isNaN(shares) || isNaN(comments) || isNaN(engagementRate)) {
            resultContainer.textContent = "Please fill in all fields correctly.";
            return;
        }

        const data = { likes, shares, comments, engagementRate };

        try {
            const response = await fetch("http://127.0.0.1:8000/diffusion", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error("Failed to connect to backend");
            }

            const result = await response.json();

            // Store in sessionStorage (not localStorage)
            sessionStorage.setItem("misinformationScore", result.misinformationScore);

            // Redirect to result page
            window.location.href = "misinformation_status.html";
        } catch (error) {
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});