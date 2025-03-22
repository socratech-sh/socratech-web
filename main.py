from flask import Flask, render_template
from utils import find_newest_posts, extract_post_title
import os


app = Flask(__name__)


@app.get("/health")
def health():
    return 200


@app.get("/")
def render_links():
    latest_posts = find_newest_posts("./posts")

    render_context = {
        "articles": [
            {"title": extract_post_title(post), "link": f"/blog/{post}"}
            for post in latest_posts
        ]
    }
    return render_template("index.html", **render_context)


@app.get("/blog")
def render_blog():
    return render_template("blog.html")


@app.get("/timeline")
def render_timeline():
    return render_template("timeline.html")


if __name__ == "__main__":
    app.run("0.0.0.0", os.getenv("PORT"))
