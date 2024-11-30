// Wait for the entire DOM to load before running the script
document.addEventListener("DOMContentLoaded", () => {

    // Get a reference to the form element in the HTML by its ID
    const form = document.getElementById("virality-form");

    // Get a reference to the container where the result or error message will be displayed
    const resultContainer = document.getElementById("result");

    // Add a 'submit' event listener to the form
    form.addEventListener("submit", async (e) => {
        // Prevent the default behavior of the form submission (like page reload)
        e.preventDefault();

        // Get values from the input fields and convert them to floating-point numbers
        const likes = parseFloat(document.getElementById("likes").value);
        const shares = parseFloat(document.getElementById("shares").value);
        const comments = parseFloat(document.getElementById("comments").value);
        const weakTies = parseFloat(document.getElementById("weak-ties").value);

        // Validate that all the input fields have been filled with valid numbers
        if (isNaN(likes) || isNaN(shares) || isNaN(comments) || isNaN(weakTies)) {
            // If any input is invalid, display an error message in the result container
            resultContainer.textContent = "Please fill in all fields correctly.";
            return; // Exit the function early
        }

        // Create an object to send the input data to the backend
        const data = { likes, shares, comments, weakTies };

        try {
            // Send the input data to the backend using a POST request
            const response = await fetch("http://127.0.0.1:8000/virality", {
                method: "POST", // HTTP method for the request
                headers: { "Content-Type": "application/json" }, // Specify that we're sending JSON data
                body: JSON.stringify(data), // Convert the data object to a JSON string for sending
            });

            // If the response from the backend is not okay, throw an error
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            // Parse the JSON response from the backend
            const result = await response.json();

            // Store the virality score returned by the backend in local storage
            localStorage.setItem("viralityScore", result.viralityScore);

            // Redirect the user to the virality score page (adjust path as necessary)
            window.location.href = 'Virality Score/virality_score.html';
        } catch (error) {
            // If there's an error (e.g., network issue), display an error message
            resultContainer.textContent = "Error connecting to backend.";
        }
    });
});
