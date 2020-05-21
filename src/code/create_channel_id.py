import pandas as pd
import codecs
from module.create_log.get_logger import get_logger
from module.youtube_details.get_channel_id import get_channel_id


def main():
    with codecs.open("../data/input/JPvideos.csv", "r", "utf-8", "ignore") as file:
        df = pd.read_table(file, delimiter=",")
        video_id = list(df["video_id"])
        display_channel_id(video_id)


def display_channel_id(video_id):
    store_channel_id = {}

    for vi in video_id[:50]:
        channel_id = get_channel_id(vi)
        get_logger().info(channel_id)
        store_channel_id[vi] = channel_id


if __name__ == '__main__':
    main()

# df.to_csv('../data/input/channel_id.csv', mode='a', header=False)
