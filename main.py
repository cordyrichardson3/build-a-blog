from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True

class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content


def get_posts():
    post1 = Post(1, "First Post", "This is my first post. Cool beans")
    post2 = Post(2, "This is my second post", "Wonder if this will work better than last time")
    post3 = Post(3, "This is my third post", "Well, third time is supposed ot be a charm")
    post4 = Post(4, "This is my fourth post", "Four posts!!! Great")
    post_list = [post1, post2, post3, post4]
    return post_list

@app.route("/")
def index():
    return render_template('index.html', post_list = get_posts())

@app.route("/add-post")
def addPost():
    return render_template('add_post.html')

@app.route("/post_item")
def post_item():
    return render_template('post_item.html')

app.run()