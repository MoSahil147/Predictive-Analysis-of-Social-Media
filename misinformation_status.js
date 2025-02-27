document.addEventListener("DOMContentLoaded", () => {
    const scoreBox = document.getElementById("score-box");
    const finalScore = sessionStorage.getItem("misinformationScore") || "N/A";
    
    scoreBox.textContent = `Score: ${finalScore}%`;
});