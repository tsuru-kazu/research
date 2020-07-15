import pandas as pd
import codecs
# 自作モジュールをインポート
from module.create_log.get_logger import get_logger  # type: ignore
from module.youtube_details.get_subcriber import get_subscriber  # type: ignore


class Subscriber:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        with codecs.open("../data/input/channel_id.csv", "r", "utf-8", "ignore") as f:
            df = pd.read_table(f, delimiter=",")
        self.channel_id = list(df["channel_id"])
        self.subscriber = {}

    def get(self):
        for idx, c_i in enumerate(self.channel_id[self.start:self.stop]):
            if c_i == "No Data":
                continue

            self.subscriber[c_i] = get_subscriber(c_i)
            print(idx, "get: ", self.subscriber[c_i])

        get_logger().info("DONE: GET Subscriber ")

    def write(self):
        c_i = list(self.subscriber.keys())
        s_c = list(self.subscriber.values())
        df = pd.DataFrame({'channel_id': c_i, 'subscriber_count': s_c})

        df.to_csv('../data/input/subscriber.csv', mode="a", header=False)

    def run(self):
        self.get()
        self.write()


if __name__ == '__main__':
    s = Subscriber(11310, 11311)
    s.run()
