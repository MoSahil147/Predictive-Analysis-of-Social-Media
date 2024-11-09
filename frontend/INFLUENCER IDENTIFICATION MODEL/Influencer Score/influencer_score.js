document.addEventListener("DOMContentLoaded", () => {
    const scoreBox = document.getElementById("score-box");

    // Define the final score (replace this with actual data from your backend)
    const finalScore = 85; // Example: 85%

    // Animation for counting up the score
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

    // Trigger the score animation after the fade-in effect
    setTimeout(updateScore, 500); // Delay to allow fade-in effect to start first
});
