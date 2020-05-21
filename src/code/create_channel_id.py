import pandas as pd
import codecs
from module.create_log.get_logger import get_logger
from module.youtube_details.get_channel_id import get_channel_id

if __name__ == '__main__':
    df = {}
    with codecs.open("../data/input/JPvideos.csv", "r", "utf-8", "ignore") as file:
        df = pd.read_table(file, delimiter=",")

        video_id = list(df["video_id"])
        channel_id = {}

        for vi in video_id[:50]:
            data = get_channel_id(vi)
            if data:
                get_logger().info(data[0]["snippet"]["channelId"])
                channel_id[vi] = data[0]["snippet"]["channelId"]

        get_logger().info(channel_id)
# df.to_csv('../data/input/channel_id.csv', mode='a', header=False)
