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

    subscriber_data = search_response["items"]

    if subscriber_data:
        subscriber_count = subscriber_data[0]["statistics"]["subscriberCount"]
        return subscriber_count
    else:
        return "No Data"


# subscriber = search_response['items'][0]['statistics']['subscriberCount']
# return subscriber
