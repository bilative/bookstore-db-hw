import pymssql
import pandas as pd
import datetime
import random


def conn_():
    return pymssql.connect(host='localhost',
                           user='sa',
                           password='Password1',
                           database='msDbProject')