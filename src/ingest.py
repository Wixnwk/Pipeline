import pandas as pd
import io
import requests
import time
import logging
from datetime import date
from config import API_KEY, RAWDATA

log = logging.getLogger(__name__)

tdate = date.today().strftime('%Y-%m-%d')

def fetch_daily(symbol:str) -> pd.DataFrame:
    try:
        response = requests.get(
            url="https://www.alphavantage.co/query?",
            params={
                "function": "TIME_SERIES_DAILY",
                "symbol": symbol,
                "datatype": "csv",
                "apikey": API_KEY,
            },
            timeout=30
        )
        if response.status_code == 204:
            raise Exception("Response body is empty")
        elif 400 <= response.status_code < 500:
            raise Exception("Error")
        else:
            df = pd.read_csv(io.StringIO(response.text))
            log.info("Successfully fetched symbol: %s, rows: %d", symbol, df.shape[0])
            return df
    except Exception as e:
        log.exception(e)


def standarise(df:pd.DataFrame, symbol:str) -> pd.DataFrame:
    normDF = df.rename(columns=lambda x : str.lower(x) if str.lower(x) != "timestamp" else "date")
    normDF.insert(loc=0, column="symbol", value=symbol)
    return normDF

def ingest(symbols:list, use_cache:bool):
    list_df = []
    for obj in symbols:
        file = f"{obj}_{tdate}.csv"
        if use_cache and (RAWDATA/file).exists():
            df = pd.read_csv(RAWDATA/file)
            list_df.append(df)
        else:
            fetched = fetch_daily(obj)
            if fetched is None:
                log.error("Symbol failed to fetch: %s", symbols)
                continue
            df = standarise(fetched, obj)
            df.to_csv(RAWDATA/file, index = False)
            list_df.append(df)
            time.sleep(0.048)
    combinedDF = pd.concat(list_df)
    return combinedDF
        
