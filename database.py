import mysql.connector
from PredictionTable import insertTableString, createTableString
from helpers import validateDatabaseConnection

def writeToDB(records, connection, myCursor):
    try:
   #executemany designed to take arrays, not an array of hashes. that would require special formatting
       myCursor.executemany(insertTableString,records)
       connection.commit()
       print('Write to db sucessful')
       connection.close()
       print('Connection closed')
    except:
       connection.rollback()
#connect to the database and return connection + cursor for interactions
def connectToDB():
    connection = mysql.connector.connect(host='localhost', user='root',passwd='root', database = 'weatherdb')
    validateDatabaseConnection(connection)
    myCursor = connection.cursor()
    myCursor.execute(createTableString)
    return connection,myCursor