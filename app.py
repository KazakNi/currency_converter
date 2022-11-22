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