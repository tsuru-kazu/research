import pandas as pd
import codecs
from module.create_log.get_logger import get_logger
from module.youtube_details.get_subcriber import get_subscriber


def main():
    channel_id = read_channel_id_csv()
    receive_subscriber = pass_subscriber(channel_id)

    get_logger().info(receive_subscriber)

    write_subscriber_to_csv(receive_subscriber)


def read_channel_id_csv():
    with codecs.open("../data/input/channel_id.csv", "r", "utf-8", "ignore") as file:
        df = pd.read_table(file, delimiter=",")
        channel_id = df['channel_id']
        return channel_id


def pass_subscriber(channel_id):
    push_subscriber = {}

    for idx, ci in enumerate(list(channel_id)[:5]):
        if ci == "No Data":
            continue

        subscriber = get_subscriber(ci)
        push_subscriber[ci] = subscriber
        print(idx, "get: " + subscriber)

    return push_subscriber


def write_subscriber_to_csv(subscriber):
    channel_id, subscriber_count = list(subscriber.keys()), list(subscriber.values())
    df = pd.DataFrame({'channel_id': channel_id, 'subscriber_count': subscriber_count})
    df.to_csv('../data/input/subscriber.csv', mode="a")


if __name__ == '__main__':
    main()
