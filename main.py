import os
import requests
from requests import post, get
import base64
import json
import webview

client_id = "7a68e9b91f494217ae1c9237863a587b"
client_secret = "922dcf0d518043d09df49b3fe2ad3ea0"

artist_search = "yes"

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64, 
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artists(artist_name):
    token = get_token()
    headers = get_auth_header(token)
    url = "https://api.spotify.com/v1/search/"
    query = f"?q={artist_name}&type=artist&limit=5"
    result = requests.get(url + query, headers=headers)
    items = result.json()["artists"]["items"]
    return items[0:5] if items else None



token = get_token()
result = search_for_artists(artist_search)

from frontend import Api, make_html

html = make_html(result)
api = Api(search_for_artists)
webview.create_window("Spotify App", html=html, js_api=api)
webview.start()

