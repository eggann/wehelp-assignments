import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        database = "website",
        password = "",
        charset = "utf8"
        )

mycursor = mydb.cursor()
mydb.close()
