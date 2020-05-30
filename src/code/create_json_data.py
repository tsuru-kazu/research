import pandas as pd
from module.youtube_details.get_json_data import get_json_data
from typing import List
import json


def main():
    df = pd.read_csv('../data/input/video_id.csv')
    video_id: List[str] = list(df["video_id"])
    youtube_data_json = {}
    for vi in video_id[:5]:
        data = get_json_data(vi)
        youtube_data_json[vi] = data

    with open('../data/external/youtube.json', 'a') as f:
        json.dump(youtube_data_json, f, ensure_ascii=False, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()
