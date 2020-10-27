import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import japanize_matplotlib

import os

def graphMaker():
    summary_csv_path = './covid_summary_data_in_japan.csv'
    # ファイルがあるか確認なければ例外発生
    if os.path.isfile(summary_csv_path):
        # グラフ化のおまじない
        plt.style.use('ggplot') 

        # データをCSVから引き抜き
        df = pd.read_csv(summary_csv_path, index_col=0)
        plt.figure()
    
        # グラフ化
        df.plot.bar()
        plt.legend(loc="upper left", fontsize=7) # 凡例表示

        # グラフのラベル付
        plt.title('日本語表示テスト', fontsize=14) # タイトル
        plt.xlabel('x軸', fontsize=14) # x軸ラベル
        plt.ylabel("y軸", fontsize=14) # y軸ラベル

        plt.savefig('./pandas_iris_line.png')     # 画像の保存
        #plt.show()                                # 画像の表示
        plt.close('all')
    else:
        # 例外を発生させる
        print('ファイルがない')
        #raise Exception

if __name__ == "__main__":
    graphMaker()