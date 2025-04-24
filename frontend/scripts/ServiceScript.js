document.addEventListener("DOMContentLoaded", () => {
    const checkUpButton = document.getElementById('check-up-button');
    const checkUpCard = document.getElementById('check-up-card');
    
    // Ensure the card is hidden by default
    checkUpCard.style.display = 'none';
    
    checkUpButton.addEventListener('click', function() {
        console.log("Button clicked");
        const currentDisplay = window.getComputedStyle(checkUpCard).display;
        console.log("Current Display:", currentDisplay);
        
        if (currentDisplay === "none") {
            checkUpCard.style.display = "block"; // Show the card
            console.log("Card shown");
        } else {
            checkUpCard.style.display = "none"; // Hide the card
            console.log("Card hidden");
        }
    });
  });