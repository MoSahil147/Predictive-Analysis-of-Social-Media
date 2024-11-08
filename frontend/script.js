function showTool(tool) {
    document.querySelectorAll('.tool-section').forEach(section => section.classList.add('hidden'));
    document.getElementById(`${tool}-tool`).classList.remove('hidden');
  }
  
  function predictVirality() {
    const likes = document.getElementById('likes').value;
    const shares = document.getElementById('shares').value;
    const comments = document.getElementById('comments').value;
    const weakTies = document.getElementById('weak-ties').value;
  
    // Example calculation for demonstration
    const viralityScore = (parseInt(likes) * 0.5 + parseInt(shares) * 0.3 + parseInt(comments) * 0.1 + parseInt(weakTies) * 0.1).toFixed(2);
  
    document.getElementById('virality-score').innerText = viralityScore;
  }
  
  function identifyInfluencer() {
    const followers = document.getElementById('followers').value;
    const posts = document.getElementById('posts').value;
    const likes = document.getElementById('likes-influencer').value;
    const comments = document.getElementById('comments-influencer').value;
    const engagementRate = document.getElementById('engagement-rate').value;
  
    // Example calculation for demonstration
    const influencerScore = (parseInt(followers) * 0.3 + parseInt(posts) * 0.2 + parseInt(likes) * 0.3 + parseInt(comments) * 0.1 + parseFloat(engagementRate) * 0.1).toFixed(2);
  
    document.getElementById('influencer-score').innerText = influencerScore;
  }
  
  function predictDiffusion() {
    const likes = document.getElementById('likes-diffusion').value;
    const shares = document.getElementById('shares-diffusion').value;
    const comments = document.getElementById('comments-diffusion').value;
    const engagementRate = document.getElementById('engagement-rate-diffusion').value;
  
    // Example calculation for demonstration
    const misinformationStatus = (parseInt(likes) * 0.4 + parseInt(shares) * 0.3 + parseInt(comments) * 0.2 + parseFloat(engagementRate) * 0.1).toFixed(2);
  
    document.getElementById('diffusion-status').innerText = misinformationStatus > 50 ? "High Risk" : "Low Risk";
  }