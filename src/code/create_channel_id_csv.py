import pandas as pd
# 自作モジュールをインポート
from module.create_log.get_logger import get_logger
from module.youtube_details.get_channel_id import get_channel_id


class ChannelId:

    def __init__(self, start, stop):
        df = pd.read_csv('../data/input/video_id.csv')
        self.video_id = list(df["video_id"])
        self.start = start
        self.stop = stop
        self.channel_id = {}

    def get(self):
        for idx, v_i in enumerate(self.video_id[self.start:self.stop]):
            self.channel_id[v_i] = get_channel_id(v_i)
            print(idx + 1, "get: " + self.channel_id[v_i])

        get_logger().info("DONE: GET Channel ID ")

    def write(self):
        v_i = list(self.channel_id.keys())
        c_i = list(self.channel_id.values())
        df = pd.DataFrame({"video_id": v_i, "channel_id": c_i})
        df.to_csv("../data/input/channel_id_no_data.csv", mode="a", header=False)

        get_logger().info("DONE: write to csv")

    def run(self):
        self.get()
        self.write()


if __name__ == '__main__':
    c = ChannelId(0, 30)
    c.run()
