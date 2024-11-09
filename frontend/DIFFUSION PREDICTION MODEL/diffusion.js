document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const resultContainer = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const likes = parseFloat(document.getElementById("likes").value);
        const shares = parseFloat(document.getElementById("shares").value);
        const comments = parseFloat(document.getElementById("comments").value);
        const engagementRate = parseFloat(document.getElementById("engagement-rate").value);

        // Basic validation
        if (isNaN(likes) || isNaN(shares) || isNaN(comments) || isNaN(engagementRate)) {
            resultContainer.textContent = "Please fill in all fields correctly.";
            return;
        }

        // Send data to backend
        const data = { likes, shares, comments, engagementRate };
        try {
            const response = await fetch("YOUR_BACKEND_URL/diffusion", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            resultContainer.textContent = `Misinformation Status: ${result.misinformationStatus}`;
        } catch (error) {
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});
