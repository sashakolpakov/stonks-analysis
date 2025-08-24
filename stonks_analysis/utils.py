import yfinance as yf
import numpy as np
import pandas as pd

def download_data(ticker, start_date=None, end_date=None, lookback_days=None):
    """
    Downloads historical stock data from Yahoo Finance.

    Args:
        ticker (str): The stock ticker symbol.
        start_date (str, optional): The start date for the data in 'YYYY-MM-DD' format. 
        end_date (str, optional): The end date for the data in 'YYYY-MM-DD' format. Defaults to today.
        lookback_days (int, optional): The number of days to look back from the end_date.

    Returns:
        pd.DataFrame: A DataFrame containing the historical stock data.
    """
    if lookback_days:
        end = pd.to_datetime(end_date) if end_date else pd.to_datetime('today')
        start = end - pd.Timedelta(days=lookback_days)
        df = yf.download(ticker, start=start, end=end, auto_adjust=False)
    else:
        df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)

    df.index = pd.to_datetime(df.index)
    return df

def compute_generic_features(df):
    """
    Computes generic financial features from stock data.

    Args:
        df (pd.DataFrame): A DataFrame with 'Close' and 'Volume' columns.

    Returns:
        pd.DataFrame: A DataFrame with 'Close', 'LogVol', and 'Return' features.
    """
    close = df["Close"].squeeze().ffill()
    vol = df.get("Volume", pd.Series(0, index=close.index)).fillna(0).squeeze()
    logvol = np.log1p(vol)
    ret = close.pct_change().fillna(0)
    return pd.DataFrame({
        "Close": close,
        "LogVol": logvol,
        "Return": ret
    }, index=close.index)
