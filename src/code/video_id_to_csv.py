import pandas as pd
import codecs


def main():
    with codecs.open("../data/input/JPvideos.csv", "r", "utf-8", "ignore") as file:
        df = pd.read_table(file, delimiter=",")
        video_id = df["video_id"]
        video_id.to_csv('../data/input/video_id.csv', mode="a")


if __name__ == '__main__':
    main()
