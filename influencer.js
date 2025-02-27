// Wait for the DOM content to be fully loaded before executing the script
document.addEventListener("DOMContentLoaded", () => {
    // Select the form element from the DOM using a query selector
    const form = document.querySelector("form");

    // Select the element where the result or error message will be displayed
    const resultContainer = document.getElementById("result");

    // Add an event listener for the form's 'submit' event
    form.addEventListener("submit", async (e) => {
        // Prevent the default form submission behavior like page reload
        e.preventDefault();

        // Retrieve and convert the form input values to floating-point numbers
        const followers = parseFloat(document.getElementById("followers").value);
        const posts = parseFloat(document.getElementById("posts").value);
        const likes = parseFloat(document.getElementById("likes").value);
        const comments = parseFloat(document.getElementById("comments").value);
        const engagementRate = parseFloat(document.getElementById("engagement-rate").value);

        // Validate the inputs to ensure all fields are filled with valid numbers
        if (isNaN(followers) || isNaN(posts) || isNaN(likes) || isNaN(comments) || isNaN(engagementRate)) {
            // If any input is invalid, display an error message in the result container
            resultContainer.textContent = "Please fill in all fields correctly.";
            return; // Exit the function to prevent further execution
        }

        // Create a data object to hold the input values for sending to the backend
        const data = { followers, posts, likes, comments, engagementRate };

        try {
            // Send the data to the backend API endpoint via a POST request
            const response = await fetch("http://127.0.0.1:8000/influencer", {
                method: "POST", // Specify the HTTP method as POST
                headers: { "Content-Type": "application/json" }, // Inform the server that the request body is JSON
                body: JSON.stringify(data), // Convert the data object to a JSON string
            });

            // Check if the response from the backend is successful
            if (!response.ok) {
                throw new Error("Failed to connect to backend"); // Throw an error if the response is not OK
            }

            // Parse the JSON response from the backend
            const result = await response.json();

            // Store the influencer score from the backend in sessionStorage for later use
            sessionStorage.setItem("influencerScore", result.influencerScore);

            // Redirect the user to a new page to display the influencer score
            window.location.href = "influencer_score.html";
        } catch (error) {
            // Handle errors (e.g., network issues) by displaying an error message
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});
