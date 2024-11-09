document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("virality-form");
    const resultContainer = document.getElementById("result");
    const formContainer = document.getElementById("form-container");
    const scoreContainer = document.getElementById("score-container");
    const scoreBox = document.getElementById("score-box");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Get form values
        const likes = parseFloat(document.getElementById("likes").value);
        const shares = parseFloat(document.getElementById("shares").value);
        const comments = parseFloat(document.getElementById("comments").value);
        const weakTies = parseFloat(document.getElementById("weak-ties").value);

        // Validation
        if (isNaN(likes) || isNaN(shares) || isNaN(comments) || isNaN(weakTies)) {
            resultContainer.textContent = "Please fill in all fields correctly.";
            return;
        }

        // Data to send to backend
        const data = { likes, shares, comments, weakTies };

        try {
            // Send data to backend
            const response = await fetch("YOUR_BACKEND_URL/virality", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });
            const result = await response.json();

            // Hide form and display score section
            formContainer.style.display = "none";
            scoreContainer.style.display = "block";

            // Animate the score
            animateScore(result.viralityScore || 90); // Use the received score, default to 90 if not available
        } catch (error) {
            resultContainer.textContent = "Error connecting to backend.";
        }
    });

    function animateScore(finalScore) {
        let currentScore = 0;
        const animationDuration = 2000; // Duration in ms (2 seconds)
        const increment = finalScore / (animationDuration / 20);

        function updateScore() {
            if (currentScore < finalScore) {
                currentScore += increment;
                scoreBox.textContent = `Score: ${Math.floor(currentScore)}%`;
                requestAnimationFrame(updateScore);
            } else {
                scoreBox.textContent = `Score: ${finalScore}%`; // Ensure it ends exactly at the final score
            }
        }

        setTimeout(updateScore, 500); // Delay to allow fade-in effect to start first
    }
});
