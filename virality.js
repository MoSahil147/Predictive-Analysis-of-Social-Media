document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("virality-form");
  const result = document.getElementById("result");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const likes    = +document.getElementById("likes").value;
    const shares   = +document.getElementById("shares").value;
    const comments = +document.getElementById("comments").value;
    const weakTies = +document.getElementById("weak-ties").value;

    if ([likes, shares, comments, weakTies].some(isNaN)) {
      result.textContent = "Please fill in all fields correctly.";
      return;
    }

    try {
      const r = await fetch(
        "https://predictive-analysis-of-social-media.onrender.com/virality",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ likes, shares, comments, weakTies }),
        }
      );

      if (!r.ok) throw new Error();
      const data = await r.json();
      sessionStorage.setItem("viralityScore", data.viralityScore);
      window.location.href = "virality_score.html";
    } catch {
      result.textContent = "Error connecting to backend.";
    }
  });
});