from googleapiclient.discovery import build
import os

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")


def get_subscriber(channel_id, api_key=YOUTUBE_API_KEY):
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id,
    ).execute()

    return search_response['items']

# subscriber = search_response['items'][0]['statistics']['subscriberCount']
# return subscriber
