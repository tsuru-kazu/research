from googleapiclient.discovery import build
import os

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")


def get_channel_id(video_id, api_key=YOUTUBE_API_KEY):
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    channel_data = search_response["items"]

    if channel_data:
        channel_id = channel_data[0]["snippet"]["channelId"]
        return channel_id
    else:
        return "No Data"


"""
api_keyに関しては、pycharmのシェルでプログラムを実行する際は、GOOGLE_APPLICATION_CREDENTIALSという環境変数を
設定するので必要ないが、ローカルのシェルで実行する際は、必要である
"""