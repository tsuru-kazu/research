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

    if 'items' in search_response:
        subscriber_data = search_response['items']
        if subscriber_data:
            subscriber_count = subscriber_data[0]["statistics"]["subscriberCount"]
            return subscriber_count
        else:
            return "No Data"
    else:
        return "No Data"


"""
api_keyに関しては、pycharmのシェルでプログラムを実行する際は、GOOGLE_APPLICATION_CREDENTIALSという環境変数を
設定するので必要ないが、ローカルのシェルで実行する際は、必要である
"""