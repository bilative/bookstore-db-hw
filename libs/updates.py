import pymssql
import pandas as pd
import datetime
import random

from .connection_ import conn_


def keepAdd(query, col, value):
    return f"""{str(query)} {col} = {value}"""


def updateTable(table, by, condition, bookName=None, authorID=None, typeID=None, publisherID=None,
                customerName=None, customerSurname=None, townID=None, phoneNumber=None):
    df = pd.DataFrame({'col': ['bookName', 'authorID', 'typeID', 'publisherID',
                               'customerName', 'customerSurname', 'townID', 'phoneNumber'],
                      'value': [bookName, authorID, typeID, publisherID,
                                customerName, customerSurname, townID, phoneNumber]
                       })

    df_ = df[df['value'].notnull()]
    query_ = f"UPDATE {table} SET"
    len_ = df_['value'].notna().sum()-1

    for i in range(len(df_)):
        query_ = keepAdd(query_, df_.iloc[i, 0], df_.iloc[i, 1])
        if (i != len_):
            query_ = query_ + ","

    query_ = f"""{query_} WHERE {by}= {condition}"""
    conn = conn_()
    cursor = conn.cursor()
    cursor.execute(query_)
    conn.commit()
    conn.close()
