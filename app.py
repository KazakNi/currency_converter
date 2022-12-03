import mysql.connector
import json
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('index.html', title='hello world')


if __name__ == "__main__":
    app.run(host="0.0.0.0")


 