import mysql.connector
import json
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_posts(post_id):
    return f'Post {escape(post_id)}'

@app.route("/")
def index() -> str:
    return "<h4>Index Page</h4>"

@app.route("/hello/")
def hello_world() -> str:
    return "<p>Hello, world!</p>"

@app.route('/widgets')
def get_widgets():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory"
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM widgets")

    row_headers = [x[0] for x in cursor.description]
    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))
    cursor.close()

    return json.dump(json_data)