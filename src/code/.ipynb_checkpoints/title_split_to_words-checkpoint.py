import MeCab
import pandas as pd
import codecs

# 分かち書きオブジェクト
tagger = MeCab.Tagger('')

# 安定するらしい
tagger.parse('')


def title_split_to_word(text):
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


def write_title_to_txt(split_words):
    with open("../data/input/title_split_words.txt", mode="w") as f:
        f.write("\n".join(split_words))


def main():
    split_words = []
    with codecs.open("../data/input/JPvideos.csv", "r", "utf-8", "ignore") as file:
        df = pd.read_table(file, delimiter=",")
    titles = list(df["title"])
    for title in titles:
        split_words.append(title_split_to_word(title))

    write_title_to_txt(split_words)


if __name__ == '__main__':
    main()
