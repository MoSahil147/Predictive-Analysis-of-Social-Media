document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const resultContainer = document.createElement("div");
    resultContainer.id = "result";
    form.appendChild(resultContainer);

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const likes = parseFloat(document.getElementById("likes").value);
        const shares = parseFloat(document.getElementById("shares").value);
        const comments = parseFloat(document.getElementById("comments").value);
        const weakTies = parseFloat(document.getElementById("weak-ties").value);

        if (isNaN(likes) || isNaN(shares) || isNaN(comments) || isNaN(weakTies)) {
            resultContainer.textContent = "Please fill in all fields correctly.";
            return;
        }

        const data = { likes, shares, comments, weakTies };
        try {
            const response = await fetch("YOUR_BACKEND_URL/virality", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            resultContainer.textContent = `Virality Score: ${result.viralityScore}`;
        } catch (error) {
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});
