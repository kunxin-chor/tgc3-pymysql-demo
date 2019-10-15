import pymysql

# represents the connection between the database and Python
connection = pymysql.connect(host='localhost', #localhost means the same machine as we are on now
    user="admin", 
    password="password",
    database="chinook"
)

cursor = connection.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT * from Employee")
for row in cursor:
    # print ("EmplyoeeID:",row[0]," is ",row[1],row[2])
    print("EmployeeID:{} is {} {}".format(row["EmployeeId"], row["LastName"], row["FirstName"]))