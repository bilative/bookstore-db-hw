import pymssql
import pandas as pd
import datetime
import random

from .connection_ import conn_


vars = {}
vars['cityTBL'] = "cityID, cityName"
vars['townTBL'] = "cityID, townName"
vars['branchTBL'] = "cityID, branchName"
vars['publisherTBL'] = "publisherName"
vars['bookTBL'] = "bookName, authorID, typeID, publisherID"
vars['authorTBL'] = "authorName, authorBirthDate"
vars['customerTBL'] = "customerName, customerSurname, phoneNumber, townID"
vars['transactionTBL'] = "customerID, bookID, branchID, count, price"
vars['typeTBL'] = "typeName"

def addFunc(table, listem):
    conn = conn_()
    cursor = conn.cursor()
    insertQuery = f"""INSERT INTO {table} ({vars[table]}) VALUES {tuple(listem)}""".replace(",)", ")")
    cursor.execute(insertQuery)
    conn.commit()
    conn.close()
    #print(insertQuery)
