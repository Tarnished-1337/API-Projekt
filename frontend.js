
// fake loading screen B)
// after intro ends
window.onload = () => {
    // simulate loading / intro
    setTimeout(() => {
        document.getElementById("intro").style.display = "none";
        document.getElementById("main").style.display = "block";
        document.getElementById("footer").style.display = "block"; 
    }, 2000); // 2 seconds
};



function searchArtist() {

    // sets the value of artist to whatever the user types into the input field
    const input = document.getElementById('artistInput');
    const artist = input.value; 


    document.getElementById('results').innerHTML = "<p style='text-align:center;'>Searching...</p>";
    input.disabled = true; // prevent typing while searching to prevent simultaneous searches

    // send the artist variable to the Python backend via PyWebView
    // pywebview calls the "search_artist" function in the Api class
    // once the results are returned, the ".then()" callback handles them
    window.pywebview.api.search_artist(artist).then(result => { 
        // result is the list returned by Python (artist names + URLs)

        input.disabled = false; // re-enable input

        // if the list returned by the spotify api is empty, then "no artists found" is displayed
        if (!result || result.length === 0) {
            document.getElementById('results').innerHTML = "<p>No artists found.</p>";
            return;

        }
        // for each artist in the result list, add a list item with its index and name
        let html = "<center><h2>Results</h2><br><ul></center>";
        result.forEach((artist, i) => {
        html += `<li class="artist-row">
                    <span class="artist-name">${i+1}. ${artist.name}</span>
                    <button class="button" onclick="window.open('${artist.url}', '_blank')">Open</button>
                </li>`;
});
html += "</ul>";
document.getElementById('results').innerHTML = html;
        
    });
}



window.addEventListener("DOMContentLoaded", () => {
    const modeButton = document.getElementById("modeButton");
    let isDark = false; // initial state

    modeButton.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
        isDark = !isDark;
    });
});


