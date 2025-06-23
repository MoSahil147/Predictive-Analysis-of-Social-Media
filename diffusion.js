document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("diffusion-form");
  const result = document.getElementById("result");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const likes          = +document.getElementById("likes").value;
    const shares         = +document.getElementById("shares").value;
    const comments       = +document.getElementById("comments").value;
    const engagementRate = +document.getElementById("engagement-rate").value;

    if ([likes, shares, comments, engagementRate].some(isNaN)) {
      result.textContent = "Please fill in all fields correctly.";
      return;
    }

    try {
      const r = await fetch(
        "https://predictive-analysis-of-social-media.onrender.com/diffusion",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ likes, shares, comments, engagementRate }),
        }
      );

      if (!r.ok) throw new Error();
      const data = await r.json();
      sessionStorage.setItem("misinformationScore", data.misinformationScore);
      window.location.href = "misinformation_status.html";
    } catch {
      result.textContent = "Error connecting to backend.";
    }
  });
});