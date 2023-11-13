import requests
import random

def get_spotify_access_token(client_id, client_secret):
    # Make a POST request to get the access token
    auth_url = "https://accounts.spotify.com/api/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(auth_url, data=payload)
    access_token = response.json()['access_token']
    return access_token


def search_songs(access_token, search_query, options):
    search_url = f"https://api.spotify.com/v1/search?q={search_query}&type=" + options
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(search_url, headers=headers)
    return response.json()


def spotifyOptions(response, options):
    result = ""
    if options == "track":
        for track in response['tracks']['items'][:5]:
            result += track['name'] + ": https://open.spotify.com/track/" + track['uri'][14:] + "\n"
        if result == "":
            return "Unable to find your request! Try Again"

        int = random.randint(1, 2)
        if int == 1:
            result += "You can also use \"album\" at the end of your request to get albums!"

    else:
        for album in response['albums']['items'][:5]:
            result += album['name'] + ": https://open.spotify.com/album/" + album['uri'][14:] + "\n"
        if result == "":
            return "Unable to find your request! Try Again"
    return result
