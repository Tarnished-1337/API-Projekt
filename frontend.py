import webview


def make_html(result):

    with open("frontend.html", "r", encoding="utf-8") as f:
        html_template = f.read()

    artist_list_html = "<ul>\n"
    for i, a in enumerate(result):
        artist_list_html += f"<li>{i+1}. {a['name']}</li>\n"
    artist_list_html += "</ul>"

    html_template = html_template.replace(
        "<div id='results'></div>",
        f"<div id='results'>{artist_list_html}</div>"
    )
    return html_template 

class Api:
    def __init__(self, search_function):
        self.search_function = search_function

    def search_artist(self, artist_name):
        if not artist_name:
            artist_name = "yes"  # default search
        result = self.search_function(artist_name)
        if not result:
            return []
        return [a["name"] for a in result]