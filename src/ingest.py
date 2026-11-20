import pandas as pd
import getCSV as gc
import requests





def getSymbol():
    print("Enter Symbol")
    return input()
def getDataType():
    print("Enter DataType")
    return input()
def getData(Symbol, datatype):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={Symbol}&apikey={APIKey}&datatype={"csv"}"
    Data = pd.read_csv(url)
    return Data

class ColumnTypes:
    date = ""
    symbol = ""
    open = ""
    high = ""
    low = ""
    close = ""
    volume = ""

symbol = gc.getSymbol()

Data = gc.getData(symbol, "a")
print(Data.head())
