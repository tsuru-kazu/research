from googleapiclient.discovery import build  # type: ignore
import os
from typing import Dict

YOUTUBE_API_KEY: str = os.environ.get("YOUTUBE_API_KEY")


def get_json_data(video_id: str, api_key: str = YOUTUBE_API_KEY):
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    channel_data: Dict = search_response

    return channel_data
