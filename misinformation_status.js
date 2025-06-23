document.addEventListener("DOMContentLoaded", () => {
    const scoreBox = document.getElementById("score-box");
    const finalScore = sessionStorage.getItem("misinformationScore");

    if (finalScore) {
        scoreBox.textContent = `Score: ${finalScore}%`;
    } else {
        scoreBox.textContent = "Score not available";
    }
});