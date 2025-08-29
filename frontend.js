function searchArtist() {
    const input = document.getElementById('artistInput');
    const artist = input.value;

    document.getElementById('results').innerHTML = "<p>Searching...</p>";
    input.disabled = true; // prevent typing while searching

    window.pywebview.api.search_artist(artist).then(result => {
        input.disabled = false; // re-enable input
        if (!result || result.length === 0) {
            document.getElementById('results').innerHTML = "<p>No artists found.</p>";
            return;
        }
        let html = "<ul>";
        result.forEach((name, i) => {
            html += `<li>${i+1}. ${name}</li>`;
        });
        html += "</ul>";
        document.getElementById('results').innerHTML = html;
    });
}


