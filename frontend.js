function searchArtist() {
    const input = document.getElementById('artistInput');
    const artist = input.value; // sets the value of artist to whatever the user types into the input field

    document.getElementById('results').innerHTML = "<p>Searching...</p>";
    input.disabled = true; // prevent typing while searching to prevent simultaneous searches

    // "sends" the artist variable value to the python backend
    // python then searches spotify for that artist and returns the list of results 
    // once the results are returned, the "then" function updates the page with the search results
    window.pywebview.api.search_artist(artist).then(result => { 

        input.disabled = false; // re-enable input

        // if the list returned by the spotify api is empty, then "no artists found" is displayed
        if (!result || result.length === 0) {
            document.getElementById('results').innerHTML = "<p>No artists found.</p>";
            return;

        }
        // for each artist in the result list, add a list item with its index and name
        let html = "<ul>";
        result.forEach((name, i) => {
            html += `<li>${i+1}. ${name}</li>`;
            
        });
        // replace the contents of the "results" div with the complete unordered list
        html += "</ul>";
        document.getElementById('results').innerHTML = html;
        
    });
}


