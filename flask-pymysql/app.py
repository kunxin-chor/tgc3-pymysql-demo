from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os

app = Flask(__name__)

@app.route('/')
def home():
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='password',
        database='chinook'
        )
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM Employee"
    cursor.execute(sql)
    return render_template("index.template.html", results=cursor)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)