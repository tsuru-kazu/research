import pandas as pd
import codecs
# 自作モジュールをインポート
from module.create_log.get_logger import get_logger  # type: ignore
from module.youtube_details.get_subcriber import get_subscriber  # type: ignore


class Subscriber:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        with codecs.open("../data/input/channel_id.csv", "r", "utf-8", "ignore") as file:
            df = pd.read_table(file, delimiter=",")
            self.channel_id = list(df["channel_id"])
        self.subscriber = {}

    def get(self):
        for idx, ci in enumerate(self.channel_id[self.start:self.stop]):
            if ci == "No Data":
                continue

            self.subscriber[ci] = get_subscriber(ci)
            print(idx, "get: ", self.subscriber[ci])

        get_logger().info("DONE: GET Subscriber ")

    def write(self):
        ci = list(self.subscriber.keys())
        sc = list(self.subscriber.values())
        df = pd.DataFrame({'channel_id': ci, 'subscriber_count': sc})

        df.to_csv('../data/input/subscriber.csv', mode="a", header=False)

    def run(self):
        self.get()
        self.write()


if __name__ == '__main__':
    s = Subscriber(990, 1020)
    s.run()
