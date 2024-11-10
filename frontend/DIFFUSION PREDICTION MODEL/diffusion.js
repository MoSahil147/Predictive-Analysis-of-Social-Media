document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("diffusion-form"); // Ensure form has the correct ID
    const resultContainer = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
        e.preventDefault(); // Prevent page reload

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
            const result = await response.json();

            if (response.ok) {
                localStorage.setItem("misinformationScore", result.misinformationScore); 
                // Correct path to the nested "misinformation_status.html"
                window.location.href = "MISINFORMATION SCORE/misinformation_status.html";
            } else {
                resultContainer.textContent = "Error calculating misinformation score.";
            }
        } catch (error) {
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});