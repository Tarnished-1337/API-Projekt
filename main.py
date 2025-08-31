import os
import requests
from requests import post, get
import base64
import json
import webview

# spotify API credentials
client_id = "7a68e9b91f494217ae1c9237863a587b"
client_secret = "922dcf0d518043d09df49b3fe2ad3ea0"

# default search query value
artist_search = "[]"

# get spotify access token
def get_token():
    # spotify requires base64-encoded client_id:client_secret for authorization
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    # url for requesting token
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64, 
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # client credentials flow
    data = {"grant_type": "client_credentials"}

    # POST request to spotify to get the token
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)

    # extract access token from teh response
    token = json_result["access_token"]
    return token

# create authorization header for requests
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# search for artists in spotify
def search_for_artists(artist_name): 
    token = get_token() # get new access token
    headers = get_auth_header(token) # prepare request headers
    url = "https://api.spotify.com/v1/search" # spotify search endpoint
    params = {"q": artist_name, "type": "artist", "limit": 5} # search parameters

    # GET request to spotify search api
    result = requests.get(url, headers=headers, params=params)

    # parse JSON response, handle errors
    try:
        data = result.json()
    except ValueError:
        return []  # invalid JSON = no results

    # extract list of artists, defualt to empty list if key is missing
    items = data.get("artists", {}).get("items", [])
    return items[:5] if items else [] # return top 5 artists or empty list




token = get_token()
result = search_for_artists(artist_search)

#load frontend and connect api

from frontend import Api, make_html

# instaniate aåi class, pass search function
api = Api(search_for_artists)

# open pywebview window with the html frontend and js api
webview.create_window("Spotify App", "frontend.html", js_api=api)
webview.start()