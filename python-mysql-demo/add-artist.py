import pymysql

# represents the connection between the database and Python
connection = pymysql.connect(host='localhost', #localhost means the same machine as we are on now
    user="admin", 
    password="password",
    database="chinook"
)

artist_name = input("Please enter the artist name > ")

cursor = connection.cursor(pymysql.cursors.Cursor)
cursor.execute("SELECT MAX(ArtistId) FROM Artist")
max_id = cursor.fetchone()[0]
next_id = max_id + 1

sql = "INSERT INTO Artist (ArtistId, Name) VALUES ({},'{}')".format(next_id, artist_name)
cursor.execute(sql)

connection.commit()