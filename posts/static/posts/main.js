console.log('Hello World')

// toggling the theme for our page
const toggleButton = document.getElementById("theme-toggle");
const body = document.body;

toggleButton.addEventListener("click", () => {
    body.classList.toggle("dark-theme");
    toggleButton.textContent = body.classList.contains("dark-theme") ? "Light Mode" : "Dark Mode";
    toggleButton.classList.toggle('light-button', !body.classList.contains("dark-theme"));
    console.log('toggle ')
    // need to implement styles change for navbar as well and other classes
});
