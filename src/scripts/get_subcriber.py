from googleapiclient.discovery import build
import os

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")


def youtube_channel_detail(channel_id, api_key):
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id,
    ).execute()

    return search_response['items'][0]


def main():

    d = youtube_channel_detail('UCHVXbQzkl3rDfsXWo8xi2qw', YOUTUBE_API_KEY)
    print(d['snippet']['title'])
    print(d['statistics']['subscriberCount'])


if __name__ == '__main__':
    main()
