import MeCab
import pandas as pd
import codecs

# 分かち書きオブジェクト
tagger = MeCab.Tagger('')

# 安定するらしい
tagger.parse('')


def description_split_to_word(text):
    node = tagger.parseToNode(text)
    terms = []
    select_conditions = ['動詞', '形容詞', '名詞']

    while node:
        # 単語
        term = node.surface
        # 品詞
        pos = node.feature.split(',')[0]
        # もし品詞が条件と一致してたら
        if pos in select_conditions:
            terms.append(term)

        node = node.next

    # 連結おじさん
    text_result = ' '.join(terms)
    return text_result


def write_description_to_csv(video_ids, split_words, titles):
    df = pd.DataFrame({"video_id": video_ids, "title": titles, "split_desc": split_words})
    df.to_csv("../data/input/description_split_words.csv")


def main():
    split_words = []
    with codecs.open("../data/input/JPvideos.csv", "r", "utf-8", "ignore") as file:
        df = pd.read_table(file, delimiter=",")

    descriptions = list(df[df["description"].notnull()]["description"])
    video_ids = list(df[df["description"].notnull()]["video_id"])
    titles = list(df[df["description"].notnull()]["title"])

    for description in descriptions:
        split_words.append(description_split_to_word(description))

    write_description_to_csv(video_ids, split_words, titles)


if __name__ == '__main__':
    main()