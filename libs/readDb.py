import pymssql
import pandas as pd

from .connection_ import conn_

def transactionList1():
    conn = conn_()
    sqlQuery = """SELECT transactionTBL.transactionID, transactionTBL.date AS [date],
		CUSTOMERTBL.customerName, BOOKTBL.bookName,BRANCHTBL.branchName,
		transactionTBL.count, transactionTBL.price from transactionTBL
            INNER JOIN CUSTOMERTBL ON transactionTBL.customerID=CUSTOMERTBL.customerID
            INNER JOIN BOOKTBL ON transactionTBL.bookID=BOOKTBL.bookID
            INNER JOIN BRANCHTBL ON transactionTBL.branchID=BRANCHTBL.branchID
		ORDER BY transactionTBL.date DESC"""
    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    if (df.shape[0] > 0):
        df['date'] = [i.strftime("%d-%m-%Y %H:%M:%S") for i in df['date']]
    return df

def bookChoose():
    conn = conn_()
    sqlQuery = """SELECT [bookID]
      ,[bookName]
      ,[authorNAME]
  FROM [msDbProject].[dbo].[bookTBL]
	INNER JOIN authorTBL ON BOOKTBL.authorID = authorTBL.authorID"""
    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    return df

# 2
# ------------------


def readTable(tablo):
    conn = conn_()

    sqlQuery = f'SELECT * FROM {tablo}'

    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    return df


def tumKitaplar():
    conn = conn_()

    sqlQuery = f"""SELECT BOOKTBL.bookID, BOOKTBL.bookName, AUTHORTBL.authorName as [authorName],
                            BOOKTBL.typeID, publisherTBL.publisherName FROM BOOKTBL 
         INNER JOIN AUTHORTBL
              ON AUTHORTBL.AUTHORID=BOOKTBL.AUTHORID
                  INNER JOIN publisherTBL
				ON BOOKTBL.publisherID=publisherTBL.publisherID
                ORDER BY BOOKTBL.bookID DESC"""

    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    return df


def search(table, criteria, id):
    conn = conn_()

    sqlQuery = f"""SELECT BOOKTBL.bookID, BOOKTBL.bookName, AUTHORTBL.authorName as [authorName],
                            BOOKTBL.typeID, publisherTBL.publisherName FROM BOOKTBL 
         INNER JOIN AUTHORTBL
              ON AUTHORTBL.AUTHORID=BOOKTBL.AUTHORID
                  INNER JOIN publisherTBL
				ON BOOKTBL.publisherID=publisherTBL.publisherID
			WHERE BOOKTBL.[{criteria}] LIKE '%{id}%'"""

    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    return df


def searchByAuthor(id):
    conn = conn_()

    sqlQuery = f"""SELECT BOOKTBL.bookID, BOOKTBL.bookName, AUTHORTBL.authorName as [authorName],
                            BOOKTBL.typeID, publisherTBL.publisherName FROM BOOKTBL 
         INNER JOIN AUTHORTBL
              ON AUTHORTBL.AUTHORID=BOOKTBL.AUTHORID
                  INNER JOIN publisherTBL
				ON BOOKTBL.publisherID=publisherTBL.publisherID
			WHERE authorTBL.[authorName] LIKE '%{id}%'"""

    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    return df

# === 3


def customerSearch3(criteria_, info_):
    conn = conn_()
    sqlQuery = f"""
    SELECT CUSTOMERTBL.customerName, CUSTOMERTBL.customerSurname, CUSTOMERTBL.customerID,
        TOWNTBL.townName, CUSTOMERTBL.phoneNumber FROM CUSTOMERTBL
        INNER JOIN TOWNTBL
            ON CUSTOMERTBL.townID=TOWNTBL.townID
            WHERE CUSTOMERTBL.{criteria_} = {info_}

    """
    print(sqlQuery)
    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    return df


def customerNullSearch3():
    conn = conn_()

    sqlQuery = f"""
    SELECT CUSTOMERTBL.customerName, CUSTOMERTBL.customerSurname, CUSTOMERTBL.customerID,
 TOWNTBL.townName, CUSTOMERTBL.phoneNumber FROM CUSTOMERTBL
        INNER JOIN TOWNTBL
            ON CUSTOMERTBL.townID=TOWNTBL.townID
		INNER JOIN cityTBL
            ON TOWNTBL.cityID=cityTBL.cityID
        ORDER BY CUSTOMERTBL.customerID DESC
    """

    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    return df


def customerTransactions3(customerID):
    conn = conn_()

    sqlQuery = f"""
    SELECT transactionTBL.date, CUSTOMERTBL.customerName, BOOKTBL.bookName, BRANCHTBL.branchName,5 AS count, transactionTBL.price
        FROM transactionTBL
            INNER JOIN CUSTOMERTBL
                ON transactionTBL.customerID= CUSTOMERTBL.customerID
            INNER JOIN BRANCHTBL
                ON transactionTBL.branchID = BRANCHTBL.branchID
            INNER JOIN BOOKTBL
                ON transactionTBL.bookID = BOOKTBL.bookID
        WHERE CUSTOMERTBL.customerID = {customerID}
        ORDER BY transactionTBL.date DESC
        """
    df = pd.read_sql(sqlQuery, conn)
    conn.close()
    if (df.shape[0] > 0):
        df['date'] = [i.strftime("%d-%m-%Y %H:%M:%S") for i in df['date']]
    return df


def customerTransactionsNull3():
    conn = conn_()

    sqlQuery = f"""
    SELECT transactionTBL.date, CUSTOMERTBL.customerName, BOOKTBL.bookName, BRANCHTBL.branchName,5 AS count, transactionTBL.price
        FROM transactionTBL
            INNER JOIN CUSTOMERTBL
                ON transactionTBL.customerID= CUSTOMERTBL.customerID
            INNER JOIN BRANCHTBL
                ON transactionTBL.branchID = BRANCHTBL.branchID
            INNER JOIN BOOKTBL
                ON transactionTBL.bookID = BOOKTBL.bookID
                ORDER BY transactionTBL.date DESC
        """
    df = pd.read_sql(sqlQuery, conn)
    if (df.shape[0] > 0):
        df['date'] = [i.strftime("%d-%m-%Y %H:%M:%S") for i in df['date']]
    conn.close()
    return df


#Page 5 
def totalNumbers():
    conn = conn_()

    transaction_ = f""" SELECT COUNT(transactionID) from transactionTBL"""
    customer_ = f""" SELECT COUNT(customerID) from customerTBL"""
    book_ = f""" SELECT COUNT(bookID) from bookTBL"""
    author_ = f""" SELECT COUNT(authorID) from authorTBL"""
    publisher_ = f""" SELECT COUNT(publisherID) from publisherTBL"""
    branch_ = f""" SELECT COUNT(branchID) from branchTBL"""
    transaction_ = pd.read_sql(transaction_, conn)
    customer_ = pd.read_sql(customer_, conn)
    book_ = pd.read_sql(book_, conn)
    author_ = pd.read_sql(author_, conn)
    publisher_ = pd.read_sql(publisher_, conn)
    branch_ = pd.read_sql(branch_, conn)
    conn.close()
    return transaction_.iloc[0,0], customer_.iloc[0,0], book_.iloc[0,0], author_.iloc[0,0], publisher_.iloc[0,0], branch_.iloc[0,0]

def priceByBranch():
    conn = conn_()

    view1 = f""" SELECT * FROM priceByBranch"""
    df = pd.read_sql(view1, conn)
    conn.close()
    return df





def branchC(city_):
    conn = conn_()

    view1 = f""" SELECT max(cityName) as city, COUNT(townName) as [# of Branch], townName
		FROM customerTBL
	INNER JOIN townTBL ON townTBL.townID = customerTBL.townID
	INNER JOIN cityTBL ON cityTBL.cityID = townTBL.cityID
	where cityName = '{city_}'
	group by townName"""
    df = pd.read_sql(view1, conn)
    conn.close()
    return df

def AuthorP():
    conn = conn_()

    view1 = f""" SELECT * FROM priceByAuthor"""
    df = pd.read_sql(view1, conn)
    conn.close()
    return df

