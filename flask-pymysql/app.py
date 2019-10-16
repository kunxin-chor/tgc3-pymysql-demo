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

@app.route("/albums")
def albums():
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='password',
        database='chinook'
        )
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM Album"
    
    # The results will be stored inside the cursor
    # after we do cursor.execute(sql)
    cursor.execute(sql)
    
    # we are passing the cursor to the template as the placeholder results
    return render_template('album.template.html', results=cursor)


@app.route('/combined')
def combined_table():
    # step 1 : Create the connection
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='password',
        database='chinook'
        )
        
    employeeCursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM Employee"
    employeeCursor.execute(sql)
    
    albumCursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM Album"
    albumCursor.execute(sql)
    
    return render_template("combined_table.template.html",
    employeeResults = employeeCursor, albumResults = albumCursor)

@app.route('/search')
def search():
    return render_template("search.template.html")
    
@app.route('/search', methods=['POST'])
def process_search():
    # try to retrieve out what the person has entered into the field
    terms = request.form["search-terms"]
    
    # create connection
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='password',
        database='chinook'
        )
        
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM Album WHERE Title LIKE '{}'".format(terms)
    cursor.execute(sql)
    
    # MAKE SURE TO COMMENT OUT THE TEST CODE
    # for each_result in cursor:
    #     print(each_result)
    return render_template("search_results.template.html", results=cursor)
    
    

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)