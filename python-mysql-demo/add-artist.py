import pymysql

# represents the connection between the database and Python
connection = pymysql.connect(host='localhost', #localhost means the same machine as we are on now
    user="admin", 
    password="password",
    database="chinook"
)