import pandas as pd
import matplotlib.pyplot as plt

import os

def graphMaker():
    summary_csv_path = './corona_summary_data_in_japan.csv'
    if os.path.isdir(summary_csv_path):
        df = pd.read_csv(summary_csv_path, index_col=0)
        print(df)
    else:
        # 例外を発生させる
        raise Exception