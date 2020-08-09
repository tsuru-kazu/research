# jupyter lab で numerical feats の相関係数を表示することが出来なかったのでスクリプトで試した

# ライブラリ読み込み
import pandas as pd
import codecs
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# メモリ削減
def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return df

# csvを読み込みデータフレームに変換


with codecs.open("../data/input/useVideos.csv", "r", "utf-8") as file:
    df = pd.read_table(file, delimiter=",")
    df = reduce_mem_usage(df)

# 不要な列が含まれているので削除
df = df.drop("Unnamed: 0", axis=1)
# 欠損値の削除
df = df.dropna()

numerical_feats = df.dtypes[df.dtypes != "category"].index

nr_rows = 12 #図を表示する際の行数
nr_cols = 3 #図を表示する際の列数

fig, axs = plt.subplots(nr_rows, nr_cols, figsize=(nr_cols*3.5,nr_rows*3))

li_num_feats = list(numerical_feats)
li_not_plot = ["category_id", "comments_disabled", "ratings_disabled"]
li_plot_num_feats = [c for c in list(numerical_feats) if c not in li_not_plot]
target = "views"

for r in range(0,nr_rows):
    for c in range(0,nr_cols):
        i = r*nr_cols+c
        if i < len(li_plot_num_feats):
            sns.regplot(df[li_plot_num_feats[i]], df[target], ax = axs[r][c])
            stp = stats.pearsonr(df[li_plot_num_feats[i]], df[target])
            str_title = "r = " + "{0:.2f}".format(stp[0]) + "      " "p = " + "{0:.2f}".format(stp[1])
            axs[r][c].set_title(str_title,fontsize=11)

plt.tight_layout()
plt.show()




