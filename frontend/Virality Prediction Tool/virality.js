document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("virality-form");
    const resultContainer = document.getElementById("result");

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
            const response = await fetch("http://127.0.0.1:8000/virality", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const result = await response.json();

            // Store the result in local storage or session storage
            localStorage.setItem("viralityScore", result.viralityScore);

            // Redirect to the score page (Update path according to structure)
            window.location.href = 'Virality Score/virality_score.html';
        } catch (error) {
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});