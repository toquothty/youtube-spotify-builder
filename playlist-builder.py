# The intent of this program is to grab videos from my youtube music
# playlist and then add them to a spotify playlist named TQ-Youtube.
# author: Thomas Toquothty, 2021

import requests
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


# Step 1: Login to youtube
def youtube_connect():
    # Directly copied from youtube data API.
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

# Step 2: Get playlist "Music"
def grab_youtube_list():
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId="PL5XuH2WwhnhuOJCgRIiHM2IMunqfA8_D8"
    )
    response = request.execute()

    print(response)

# Step 3: Create spotify playlist, TQ-Youtube
def create_playlist():
    pass

# Step 4: Search spotify for song
def search_spotify():
    pass

# Step 5: Add the song to TQ-Youtube.
def add_song_playlist():
    pass

youtube_connect()
grab_youtube_list()
create_playlist()
search_spotify()
add_song_playlist()