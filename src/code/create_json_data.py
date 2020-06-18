import pandas as pd
from module.youtube_details.get_json_data import get_json_data
from typing import List
import json


def main():
    df = pd.read_csv('../data/input/video_id.csv')
    video_id: List[str] = list(df["video_id"])
    youtube_data_json = {}
    for idx, vi in enumerate(video_id[120:150]):
        youtube_data_json[vi] = get_json_data(vi)
        print(idx+1, "get")

    with open('../data/external/youtube5.json', 'a') as f:
        json.dump(youtube_data_json, f, ensure_ascii=False, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()
