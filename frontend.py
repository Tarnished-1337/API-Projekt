import webview


def make_html(result):

    artist_list_html = "<ul>\n"
    for i, a in enumerate(result):
        artist_list_html += f"<li>{i+1}. {a['name']}</li>\n"
    artist_list_html += "</ul>"

    # Lite Front-End HTML 
    html = """
    <html>
    <head>
    <title>Spotify App</title>

            <script>
            <!--Javascript-->            
            function searchArtist() { 
                const artist = document.getElementById('artistInput').value; // Hämtar värdet från sökfältet med id "artistInput"
                window.pywebview.api.search_artist(artist).then(response => {
                    // results är resultatet av sökningen via spotifys API och visar listan av resultat
                    document.getElementById('results').innerHTML = response; 
                });
            }
        </script>
    </head>
    <body>
        <h1>Search for an Artist</h1>
        <input type="text" id="artistInput" placeholder="Enter artist name"/>
        <button onclick="searchArtist()">Search</button>
        <div id="results"></div>
    </body>
    </html>

    """
    return html

class Api:
    def __init__(self, search_function):
        self.search_function = search_function

    def search_artist(self, artist_name):

        result = self.search_function(artist_name)

        if not result:
            return "<p>No artists found.</p>"
        html_list = "<ul>"
        for i, a in enumerate(result):
            html_list += f"<li>{i+1}. {a['name']}</li>"
        html_list += "</ul>"
        return html_list

