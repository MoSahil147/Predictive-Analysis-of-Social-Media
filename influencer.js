document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("influencer-form");
  const result = document.getElementById("result");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const followers      = +document.getElementById("followers").value;
    const posts          = +document.getElementById("posts").value;
    const likes          = +document.getElementById("likes").value;
    const comments       = +document.getElementById("comments").value;
    const engagementRate = +document.getElementById("engagement-rate").value;

    if ([followers, posts, likes, comments, engagementRate].some(isNaN)) {
      result.textContent = "Please fill in all fields correctly.";
      return;
    }

    try {
      const r = await fetch(
        "https://predictive-analysis-of-social-media.onrender.com/influencer",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ followers, posts, likes, comments, engagementRate }),
        }
      );

      if (!r.ok) throw new Error();
      const data = await r.json();
      sessionStorage.setItem("influencerScore", data.influencerScore);
      window.location.href = "influencer_score.html";
    } catch {
      result.textContent = "Error connecting to backend.";
    }
  });
});