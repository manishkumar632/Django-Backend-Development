document.addEventListener("DOMContentLoaded", function () {
    const csrfTokenInput = document.querySelector(
        'input[name="csrfmiddlewaretoken"]'
    );
    if (csrfTokenInput) {
        console.log("CSRF Token:", csrfTokenInput.value);
    } else {
        console.log("CSRF Token input not found.");
    }
});

const renderpage = async () => {
    const renderPage = document.getElementById("renderHTML");
    if (renderPage) {
        renderPage.remove();
    }
    const page = await fetch("countword");
    const text = await page.text();
    console.log(text);
    const div = document.createElement("div");
    div.id = "renderHTML";
    div.innerHTML = text;
    document.getElementById("render").appendChild(div);
};