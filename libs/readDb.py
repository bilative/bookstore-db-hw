import pymssql
import pandas as pd

from .connection_ import conn_


def readFunc(query, data=None):
    #readFunc(query, data = [repr('first'), 2])
    conn = conn_()
    if data:
        query = query % tuple(data)
    df = pd.read_sql(query, conn)
    conn.close()
    if (query in [list_of_transactions, customer_trans]) & (df.shape[0] > 0):
        df['date'] = [i.strftime("%d-%m-%Y %H:%M:%S") for i in df['date']]
        return df
    return df


all_table = "SELECT * FROM %s"

bookChoose = """SELECT [bookID] ,[bookName] ,[authorNAME]
        FROM [msDbProject].[dbo].[bookTBL]
            INNER JOIN authorTBL ON BOOKTBL.authorID = authorTBL.authorID
        """

all_books = """SELECT BOOKTBL.bookID, BOOKTBL.bookName, AUTHORTBL.authorName as [authorName],
        BOOKTBL.typeID, publisherTBL.publisherName FROM BOOKTBL 
            INNER JOIN AUTHORTBL ON AUTHORTBL.AUTHORID=BOOKTBL.AUTHORID
            INNER JOIN publisherTBL ON BOOKTBL.publisherID=publisherTBL.publisherID
        ORDER BY BOOKTBL.bookID DESC
        """
search = """SELECT BOOKTBL.bookID, BOOKTBL.bookName, AUTHORTBL.authorName as [authorName],
        BOOKTBL.typeID, publisherTBL.publisherName FROM BOOKTBL 
            INNER JOIN AUTHORTBL ON AUTHORTBL.AUTHORID=BOOKTBL.AUTHORID
            INNER JOIN publisherTBL ON BOOKTBL.publisherID=publisherTBL.publisherID
		WHERE BOOKTBL.[%s] LIKE '%%%s%%'
        """
search_by_author = """SELECT BOOKTBL.bookID, BOOKTBL.bookName, AUTHORTBL.authorName as [authorName],
        BOOKTBL.typeID, publisherTBL.publisherName FROM BOOKTBL 
            INNER JOIN AUTHORTBL ON AUTHORTBL.AUTHORID=BOOKTBL.AUTHORID
            INNER JOIN publisherTBL ON BOOKTBL.publisherID=publisherTBL.publisherID
		WHERE authorTBL.[authorName] LIKE '%%%s%%'
        """
customer_search = """SELECT CUSTOMERTBL.customerName, CUSTOMERTBL.customerSurname,
        CUSTOMERTBL.customerID, TOWNTBL.townName, CUSTOMERTBL.phoneNumber FROM CUSTOMERTBL
            INNER JOIN TOWNTBL ON CUSTOMERTBL.townID=TOWNTBL.townID
        WHERE CUSTOMERTBL.%s = %s
        """
customer_n_search = """SELECT CUSTOMERTBL.customerName, CUSTOMERTBL.customerSurname, CUSTOMERTBL.customerID,
        TOWNTBL.townName, CUSTOMERTBL.phoneNumber FROM CUSTOMERTBL
            INNER JOIN TOWNTBL ON CUSTOMERTBL.townID=TOWNTBL.townID
		    INNER JOIN cityTBL ON TOWNTBL.cityID=cityTBL.cityID
        ORDER BY CUSTOMERTBL.customerID DESC
        """
cust_trans_search = """SELECT transactionTBL.date, CUSTOMERTBL.customerName, BOOKTBL.bookName, BRANCHTBL.branchName,
        5 AS count, transactionTBL.price FROM transactionTBL
            INNER JOIN CUSTOMERTBL ON transactionTBL.customerID= CUSTOMERTBL.customerID
            INNER JOIN BRANCHTBL ON transactionTBL.branchID = BRANCHTBL.branchID
            INNER JOIN BOOKTBL ON transactionTBL.bookID = BOOKTBL.bookID
        ORDER BY transactionTBL.date DESC
        """

list_of_transactions = """SELECT transactionTBL.transactionID, transactionTBL.date AS [date],
		CUSTOMERTBL.customerName, BOOKTBL.bookName,BRANCHTBL.branchName,
		transactionTBL.count, transactionTBL.price from transactionTBL
            INNER JOIN CUSTOMERTBL ON transactionTBL.customerID=CUSTOMERTBL.customerID
            INNER JOIN BOOKTBL ON transactionTBL.bookID=BOOKTBL.bookID
            INNER JOIN BRANCHTBL ON transactionTBL.branchID=BRANCHTBL.branchID
		ORDER BY transactionTBL.date DESC"""

customer_trans = """SELECT transactionTBL.date, CUSTOMERTBL.customerName, BOOKTBL.bookName,
        BRANCHTBL.branchName,5 AS count, transactionTBL.price FROM transactionTBL
            INNER JOIN CUSTOMERTBL ON transactionTBL.customerID= CUSTOMERTBL.customerID
            INNER JOIN BRANCHTBL ON transactionTBL.branchID = BRANCHTBL.branchID
            INNER JOIN BOOKTBL ON transactionTBL.bookID = BOOKTBL.bookID
        WHERE CUSTOMERTBL.customerID = %s
            ORDER BY transactionTBL.date DESC
        """

branch_table = """ SELECT max(cityName) as city, COUNT(townName) as [# of Branch],
        townName FROM customerTBL
        INNER JOIN townTBL ON townTBL.townID = customerTBL.townID
        INNER JOIN cityTBL ON cityTBL.cityID = townTBL.cityID
	        where cityName = '%s'
	    group by townName"""


tables = ['transactionTBL', 'customerTBL', 'bookTBL',
          'authorTBL', 'publisherTBL', 'branchTBL']


def totalCounts(tables=tables):
    numbs = {}
    for table, i in zip(tables, range(1, len(tables)+1)):
        numbs[f"no{i}"] = pd.read_sql(
            f"SELECT COUNT(*) from {table}", conn_()).iloc[0, 0]

    return numbs
