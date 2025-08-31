import webview


def make_html(result):

    # opens frontend.html in read mode and reads its entire content as string encoded with UTF-8
    # the string is then stored in the variable html_template, which is then manipulated through injection 
    with open("frontend.html", "r", encoding="utf-8") as f:
        html_template = f.read()

    # creates the unordered list and loops through results with index
    artist_list_html = "<ul>\n"
    for i, a in enumerate(result):
        artist_list_html += f"<li>{i+1}. {a['name']}</li>\n"
    artist_list_html += "</ul>"

    # replaces placeholder <div id='results'></div> OR current search results with the new list of artists in the currently running instance
    html_template = html_template.replace(
        "<div id='results'></div>",
        f"<div id='results'>{artist_list_html}</div>"
    )
    # returns the manipulated html_template string to be rendered in the webview
    return html_template 

class Api:
    def __init__(self, search_function):
        self.search_function = search_function

    def search_artist(self, artist_name):

        # "artist_name" receives the value typed into the input field
        # through PyWebView. The JS code does:
            #   const artist = document.getElementById('artistInput').value;
            #   window.pywebview.api.search_artist(artist)
            # PyWebView automatically passes "artist" as the argument "artist_name".

        result = self.search_function(artist_name)
        # if no artists are found, an empty list is returned
        if not result:
            return []
        # if artists are found, a list of dicts is created, containing artist names and spotify URL
        return [{"name": a["name"], "url": a["external_urls"]["spotify"]} for a in result]