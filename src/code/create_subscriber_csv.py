import pandas as pd
import codecs
from typing import List, Dict, NoReturn
# 自作モジュールをインポート
from module.create_log.get_logger import get_logger  # type: ignore
from module.youtube_details.get_subcriber import get_subscriber  # type: ignore


def main() -> NoReturn:
    channel_id_list = read_channel_id_csv()
    receive_subscriber = pass_subscriber(channel_id_list)
    get_logger().info(receive_subscriber)

    write_subscriber_to_csv(receive_subscriber)


def read_channel_id_csv() -> List[str]:
    with codecs.open("../data/input/channel_id.csv", "r", "utf-8", "ignore") as file:
        df = pd.read_table(file, delimiter=",")
        channel_id_list: List[str] = list(df['channel_id'])
        return channel_id_list


def pass_subscriber(channel_id_list: List[str]) -> Dict[str, str]:
    push_subscriber: Dict[str, str] = {}

    for idx, channel_id in enumerate(channel_id_list[:5]):
        if channel_id == "No Data":
            continue

        subscriber: str = get_subscriber(channel_id)
        push_subscriber[channel_id] = subscriber
        print(idx, "get: ", subscriber)

    return push_subscriber


def write_subscriber_to_csv(subscriber_dict: Dict) -> NoReturn:
    channel_id: List[str] = list(subscriber_dict.keys())
    subscriber_count: List[int] = list(subscriber_dict.values())

    df = pd.DataFrame({'channel_id': channel_id, 'subscriber_count': subscriber_count})

    df.to_csv('../data/input/subscriber.csv', mode="a")


if __name__ == '__main__':
    main()
