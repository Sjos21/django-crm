import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='ShivuJoshi21'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE shivu_dcrm")
print("hello")