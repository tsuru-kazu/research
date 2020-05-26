import pandas as pd
import codecs
from module.create_log.get_logger import get_logger
from module.youtube_details.get_channel_id import get_channel_id


def main():
    with codecs.open("../data/input/JPvideos.csv", "r", "utf-8", "ignore") as file:
        df = pd.read_table(file, delimiter=",")
        video_id = list(df["video_id"])
        receive_channel_id = pass_channel_id(video_id)
        write_channel_id_to_csv(receive_channel_id)


def pass_channel_id(video_id):
    push_channel_id = {}
    # 一度に回すループ数は30ぐらい
    for idx, vi in enumerate(video_id[420:450]):
        channel_id = get_channel_id(vi)
        push_channel_id[vi] = channel_id
        print(idx, "get: " + channel_id)

    get_logger().info("DONE: GET Channel ID ")

    return push_channel_id


def write_channel_id_to_csv(rci):
    video_id, channel_id = list(rci.keys()), list(rci.values())
    df = pd.DataFrame({"video_id": video_id, "channel_id": channel_id})
    df.to_csv("../data/input/channel_id.csv", mode="a", header=False)

    get_logger().info("DONE: write to csv")


if __name__ == '__main__':
    main()
