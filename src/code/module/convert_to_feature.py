import pandas as pd

from base import Feature, get_arguments, generate_features

Feature.dir = 'features'


class FamilySize(Feature):
    def create_features(self):
        self.train["id"] = train["video_id"]
        self.test['category_id'] = train["category_id"]


if __name__ == '__main__':
    args = get_arguments()

    train = pd.read_csv('./data/input/CAvideos.csv')
    test = pd.read_csv('./data/input/CAvideos.csv')

    generate_features(globals(), args.force)

"""
実行方法
codeディレクトリの中で、
python -m module/convert_feature
を実行する
"""