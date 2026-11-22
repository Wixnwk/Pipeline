import pandas as pd
import logging
from config import SCHEMA, SchemaError

log = logging.getLogger(__name__)

def check_schema(df:pd.DataFrame):
    try:
        diff = df.columns.difference(SCHEMA)
        if diff > 0:
            raise SchemaError(diff)
    except SchemaError as e:
        log.exception(e)


def validate(df:pd.DataFrame):
    localDF = df.copy()
    #parse date and number
    for item in SCHEMA[1:]:
        if item == "date":
            localDF[item] = pd.to_datetime(localDF[item], errors="coerce")
        else:
            localDF[item] = pd.to_numeric(localDF[item], errors="coerce")
    #check price and volume isn't negative