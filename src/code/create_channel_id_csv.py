import pandas as pd
from typing import NoReturn, Dict, List
# 自作モジュールをインポート
from module.create_log.get_logger import get_logger
from module.youtube_details.get_channel_id import get_channel_id


def main() -> NoReturn:
    df = pd.read_csv('../data/input/video_id.csv')
    video_id: List[str] = list(df["video_id"])
    receive_channel_id: Dict[str, str] = fetch_channel_id(video_id)
    write_channel_id_to_csv(receive_channel_id)


def fetch_channel_id(video_id) -> Dict[str, str]:
    push_channel_id: Dict[str, str] = {}
    # 一度に回すループ数は30ぐらい
    for idx, vi in enumerate(video_id[7210:7240]):
        channel_id: str = get_channel_id(vi)
        push_channel_id[vi] = channel_id
        print(idx+1, "get: " + channel_id)

    get_logger().info("DONE: GET Channel ID ")

    return push_channel_id


def write_channel_id_to_csv(rci: Dict[str, str]) -> NoReturn:
    video_id: List[str] = list(rci.keys())
    channel_id: List[str] = list(rci.values())
    df = pd.DataFrame({"video_id": video_id, "channel_id": channel_id})
    df.to_csv("../data/input/channel_id.csv", mode="a", header=False)

    get_logger().info("DONE: write to csv")


if __name__ == '__main__':
    main()
