#import akshare as ak
#stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907', adjust="")
#print(stock_zh_a_hist_df)
import akshare as ak
from pandas import Series,DataFrame
import pandas as pd
#前复权拉去股票数
def fetch_index(index):
    stock_df = ak.stock_zh_index_daily_tx(symbol=index)
    stock_high_max = DataFrame([stock_df['high'].shift(1), stock_df['high']]).T.max(axis=1)
    stock_low_min = DataFrame([stock_df['low'].shift(1), stock_df['low']]).T.min(axis=1)
    stock_df["pcnt"] = (stock_df["close"] - stock_df["close"].shift(1)) / stock_df['close'] * 100
    stock_df["pcnt"].fillna(0)
    stock_df["pcnt_real_time"] = (stock_high_max - stock_low_min) / stock_df['close'] * 100
    stock_df.to_csv(index + ".csv", date_format='%Y-%m-%d')
    print(stock_df)

if __name__ == '__main__':
    index_list = ["sh510500", "sh512010", "sz159928"]
    for index in index_list:
        fetch_index(index)