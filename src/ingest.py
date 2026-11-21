import pandas as pd
import io
import requests
from config import API_KEY


def fetch_daily(symbol:str):
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
            return df
    except Exception as e:
        print(e)


def standarise():
    pass

def ingest():
    pass






# def getSymbol():
#     print("Enter Symbol")
#     return input()
# def getDataType():
#     print("Enter DataType")
#     return input()
# def getData(Symbol, datatype):
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={Symbol}&apikey={APIKey}&datatype={"csv"}"
#     Data = pd.read_csv(url)
#     return Data

# class ColumnTypes:
#     date = ""
#     symbol = ""
#     open = ""
#     high = ""
#     low = ""
#     close = ""
#     volume = ""

# symbol = gc.getSymbol()

# Data = gc.getData(symbol, "a")
# print(Data.head())
