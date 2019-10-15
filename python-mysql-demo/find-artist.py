import pymysql

# represents the connection between the database and Python
connection = pymysql.connect(host='localhost', #localhost means the same machine as we are on now
    user="admin", 
    password="password",
    database="chinook"
)

cursor = connection.cursor(pymysql.cursors.DictCursor)

artist_name = input("Please enter the artist name > ")
sql = "SELECT * FROM Artist WHERE Name LIKE '%{}%'".format(artist_name)
cursor.execute(sql)
for each_result in cursor:
    print(each_result['Name'])

