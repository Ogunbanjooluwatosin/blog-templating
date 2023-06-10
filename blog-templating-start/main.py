from flask import Flask, render_template

import requests

blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get(blog_endpoint)
    all_posts = response.json()
    return render_template("index.html", all_posts=all_posts)


@app.route("/blog/<blog_id>")
def blog(blog_id):
    print(blog_id)
    response = requests.get(blog_endpoint)
    all_posts = response.json()
    return render_template("post.html",all_posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
