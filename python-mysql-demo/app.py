import pymysql

# represents the connection between the database and Python
connection = pymysql.connect(host='localhost',
    user="admin",
    password="password",
    database="Chinook"
)