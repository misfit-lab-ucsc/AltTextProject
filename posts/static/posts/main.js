console.log('Hello World')

// toggling the theme for our page
const toggleButton = document.getElementById("theme-toggle");
const body = document.querySelector("body");

toggleButton.addEventListener("click", () => {
    console.log("clicked");
    body.classList.toggle("dark-theme");

    // get current text content of the button
    const currentText = toggleButton.textContent;

    // update text based on current state of body class
    if (body.classList.contains("dark-theme")) {
        toggleButton.textContent = "Light Mode";
    } else {
        toggleButton.textContent = "Dark Mode";
    }
});
