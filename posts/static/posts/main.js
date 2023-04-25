console.log('Hello World')

// toggling the theme for our page
const toggleButton = document.getElementById("theme-toggle");
const body = document.body;
// document.querySelector("body");

toggleButton.addEventListener("click", () => {

    body.classList.toggle("dark-theme");
    toggleButton.textContent = body.classList.contains("dark-theme") ? "Light Mode" : "Dark Mode";
  
    toggleButton.classList.toggle('light-button', !body.classList.contains("dark-theme"));
    console.log('toggle ')



    // console.log("clicked");
    // body.classList.toggle("dark-theme");
    // get current text content of the button
    // const currentText = toggleButton.textContent;
    // update text based on current state of body class
    // if (body.classList.contains("dark-theme")) {
    //     console.log('light style')
    //     toggleButton.textContent = "Light Mode";
    // } else {
    //     console.log('dark style')
    //     toggleButton.textContent = "Dark Mode";
    //     toggleButton.classList.toggle('light-button');
    // }
});
