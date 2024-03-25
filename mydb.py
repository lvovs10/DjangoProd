import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Lvovsergei5!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")
print('All done!')