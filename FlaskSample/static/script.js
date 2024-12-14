// Highlight table rows on hover
document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll("table tbody tr");
    rows.forEach((row) => {
        row.addEventListener("mouseover", () => {
            row.style.backgroundColor = "#f0f8ff"; // Light blue on hover
        });
        row.addEventListener("mouseout", () => {
            row.style.backgroundColor = ""; // Reset background color
        });
    });
});

// Add interactivity to buttons (if needed)
const buttons = document.querySelectorAll("button");
buttons.forEach((button) => {
    button.addEventListener("mouseover", () => {
        button.style.backgroundColor = "#0056b3"; // Darker blue on hover
    });
    button.addEventListener("mouseout", () => {
        button.style.backgroundColor = "#007BFF"; // Default blue
    });
});
