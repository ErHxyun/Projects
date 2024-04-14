# %%
import datetime as dt

# Import style to make plots
import matplotlib.pyplot as plt

# Make it look better
# Import the candle stick graph
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# Import pandas, datareader, and yahoo finance
import pandas as pd
from pandas_datareader import data as web
import yfinance as yfin

style.use("ggplot")

# Set the starting time
start = dt.datetime(2024, 1, 1)
end = dt.datetime(2024, 3, 31)

# Set the data frame
yfin.pdr_override()
df = web.get_data_yahoo("TSLA", start, end)

# Convert the data into a csv file
df.to_csv("Tesla.csv")

# Import a csv file and read it
# Can be converted into many different formats
df = pd.read_csv("Tesla.csv", parse_dates=True, index_col=0)

# Open high low close value
df_ohlc = df["Adj Close"].resample("10D").ohlc()
df_volume = df["Volume"].resample("10D").sum()

# Reset the index for dohlc
df_ohlc.reset_index(inplace=True)
df_ohlc["Date"] = df_ohlc["Date"].map(mdates.date2num)


# Visualize the data
# df["Adj Close"].plot()
# plt.show()

# Add new columns to pandas
# 100 moving average is the average of today's price and 99 prior days' prices
# df["100 moving average"] = df["Adj Close"].rolling(window=100, min_periods=0).mean()

# Drop all the N/A
# df.dropna(inplace=True)


# Create two axises for further visualization
axis1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
axis2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=axis1)
axis1.xaxis_date()

candlestick_ohlc(
    axis1,
    df_ohlc.values,
    width=2,
    colorup="g",
)

axis2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

# Visualize the axis created
# X of the plot will be the index of the datetime;
# axis1.plot(df.index, df["Adj Close"])
# axis1.plot(df.index, df["100 moving average"])
# axis2.bar(df.index, df["Volume"])

plt.show()
# %%
