import pymssql
import pandas as pd

from .connection_ import conn_

def deleteFunc(table_name, key, value):
    conn = conn_()
    cursor = conn.cursor()
    delete_query = f"DELETE {table_name} WHERE {key} = {value}"
    cursor.execute(delete_query)
    conn.commit()
    conn.close()

