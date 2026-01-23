// This script adds some interactive features to the introduction page.

document.addEventListener("DOMContentLoaded", () => {
    // This event listener waits for the page to be fully loaded before running the script.

    // This function creates a parallax effect on the background image of the main section.
    // As the user scrolls down, the background image moves at a slower speed, creating a sense of depth.
    window.addEventListener("scroll", () => {
        const scrollPosition = window.pageYOffset;
        const mainSection = document.querySelector(".main");
        mainSection.style.backgroundPositionY = `${scrollPosition * 0.5}px`; // The multiplier (0.5) controls the speed of the parallax effect.
    });

    // This function adds a hover animation to the "What We Offer" cards.
    // When the user hovers over a card, it scales up slightly to provide visual feedback.
    const offerCards = document.querySelectorAll(".offer-card");
    offerCards.forEach(card => {
        card.addEventListener("mouseover", () => {
            card.style.transform = "scale(1.05)";
            card.style.transition = "transform 0.3s ease";
        });
        card.addEventListener("mouseleave", () => {
            card.style.transform = "scale(1)";
        });
    });
});