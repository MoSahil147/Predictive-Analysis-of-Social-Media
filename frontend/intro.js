document.addEventListener("DOMContentLoaded", () => {
    // Parallax effect on scroll
    window.addEventListener("scroll", () => {
        const scrollPosition = window.pageYOffset;
        const mainSection = document.querySelector(".main");
        mainSection.style.backgroundPositionY = `${scrollPosition * 0.5}px`; // Adjust multiplier for parallax speed
    });

    // Hover animation for "What We Offer" cards
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
