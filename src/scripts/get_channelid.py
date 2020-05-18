from googleapiclient.discovery import build
import os

YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')


def youtube_channel_detail(video_id, api_key):
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    return search_response['items'][0]


def main():

    d = youtube_channel_detail('4cRanIowkTE', YOUTUBE_API_KEY)
    print(d['snippet']['channelId'])


if __name__ == '__main__':
    main()
