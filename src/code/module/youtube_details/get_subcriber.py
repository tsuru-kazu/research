from googleapiclient.discovery import build # type: ignore
import os
from typing import Union

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")


def get_subscriber(channel_id: str, api_key: str = YOUTUBE_API_KEY) -> Union[str, int]:
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id,
    ).execute()

    subscriber_count: Union[str, int]

    if 'items' in search_response:
        subscriber_data = search_response['items']
        if subscriber_data:
            subscriber_count = int(subscriber_data[0]["statistics"]["subscriberCount"])
            return subscriber_count
        else:
            subscriber_count = "No Data"
            return subscriber_count
    else:
        subscriber_count = "No Data"
        return subscriber_count


"""
api_keyに関しては、pycharmのシェルでプログラムを実行する際は、GOOGLE_APPLICATION_CREDENTIALSという環境変数を
設定するので必要ないが、ローカルのシェルで実行する際は、必要である
"""